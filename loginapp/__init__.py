# loginapp/__init__.py
"""
EcoCleanUp Hub - COMP639 S1 2026 Individual Assignment
Full Flask application with role-based access, PostgreSQL, bcrypt passwords
Author: Chenghao (your student ID)
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from flask_bcrypt import Bcrypt
from functools import wraps
from datetime import datetime, timedelta
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import uuid

# ────────────────────────────────────────────────
# 配置（从 connect.py 读取或硬编码用于开发）
# ────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production-2026'
app.config['UPLOAD_FOLDER'] = 'static/profile_images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB max

bcrypt = Bcrypt(app)

# 确保上传目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# ────────────────────────────────────────────────
# 数据库连接（建议从 connect.py 导入，这里简化演示）
# ────────────────────────────────────────────────
def get_db_connection():
    conn = psycopg2.connect(
        dbname="ecocleanup",
        user="your_pg_user",  # ← 修改为你的 PythonAnywhere / 本地 用户名
        password="your_pg_password",  # ← 修改
        host="your-host",  # localhost 或 PythonAnywhere 提供的 host
        port=5432,
        cursor_factory=RealDictCursor
    )
    return conn


# ────────────────────────────────────────────────
# 辅助函数
# ────────────────────────────────────────────────

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('请先登录', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        @login_required
        def decorated_function(*args, **kwargs):
            if session.get('role') not in roles:
                flash('您没有权限访问此页面', 'danger')
                return redirect(url_for('home'))
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def get_current_user():
    if 'user_id' not in session:
        return None
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = %s", (session['user_id'],))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user


# ────────────────────────────────────────────────
# 路由 - 首页
# ────────────────────────────────────────────────
@app.route('/')
def home():
    user = get_current_user()

    upcoming = None
    if user and user['role'] == 'volunteer':
        conn = get_db_connection()
        cur = conn.cursor()
        # 查找 7 天内即将参加的活动
        cur.execute("""
                    SELECT e.*, er.attendance
                    FROM events e
                             JOIN eventregistrations er ON e.event_id = er.event_id
                    WHERE er.volunteer_id = %s
                      AND e.event_date >= CURRENT_DATE
                      AND e.event_date <= CURRENT_DATE + INTERVAL '7 days'
                    ORDER BY e.event_date, e.start_time
                        LIMIT 3
                    """, (user['user_id'],))
        upcoming = cur.fetchall()
        cur.close()
        conn.close()

    return render_template('home.html', user=user, upcoming=upcoming)


# ────────────────────────────────────────────────
# 登录
# ────────────────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND status = 'active'", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and bcrypt.check_password_hash(user['password_hash'], password):
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash('登录成功！', 'success')
            return redirect(url_for('home'))
        else:
            flash('用户名或密码错误，或账号未激活', 'danger')

    return render_template('login.html')


# ────────────────────────────────────────────────
# 注册（仅志愿者可注册）
# ────────────────────────────────────────────────
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        home_address = request.form.get('home_address')
        contact_number = request.form.get('contact_number')
        interests = request.form.get('environmental_interests')

        if len(password) < 8:
            flash('密码至少 8 位', 'danger')
            return redirect(url_for('register'))

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                        INSERT INTO users (username, password_hash, full_name, email, home_address, contact_number,
                                           environmental_interests, role)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, 'volunteer')
                        """, (username, password_hash, full_name, email, home_address, contact_number, interests))
            conn.commit()
            flash('注册成功！请登录', 'success')
            return redirect(url_for('login'))
        except psycopg2.IntegrityError:
            conn.rollback()
            flash('用户名或邮箱已被使用', 'danger')
        finally:
            cur.close()
            conn.close()

    return render_template('register.html')


# ────────────────────────────────────────────────
# 登出
# ────────────────────────────────────────────────
@app.route('/logout')
def logout():
    session.clear()
    flash('已登出', 'info')
    return redirect(url_for('home'))


# ────────────────────────────────────────────────
# 个人资料
# ────────────────────────────────────────────────
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = get_current_user()

    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        home_address = request.form.get('home_address')
        contact_number = request.form.get('contact_number')
        interests = request.form.get('environmental_interests')

        profile_image = user['profile_image']
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and allowed_file(file.filename):
                ext = file.filename.rsplit('.', 1)[1].lower()
                filename = f"{uuid.uuid4()}.{ext}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                profile_image = filename

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    UPDATE users
                    SET full_name               = %s,
                        email                   = %s,
                        home_address            = %s,
                        contact_number          = %s,
                        environmental_interests = %s,
                        profile_image           = %s
                    WHERE user_id = %s
                    """, (full_name, email, home_address, contact_number, interests, profile_image, user['user_id']))
        conn.commit()
        cur.close()
        conn.close()

        flash('个人资料已更新', 'success')
        return redirect(url_for('profile'))

    return render_template('profile.html', user=user)


# ────────────────────────────────────────────────
# 修改密码
# ────────────────────────────────────────────────
@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    user = get_current_user()

    if request.method == 'POST':
        old_pw = request.form.get('old_password')
        new_pw = request.form.get('new_password')
        confirm_pw = request.form.get('confirm_password')

        if not bcrypt.check_password_hash(user['password_hash'], old_pw):
            flash('旧密码错误', 'danger')
            return redirect(url_for('change_password'))

        if new_pw != confirm_pw:
            flash('两次新密码不一致', 'danger')
            return redirect(url_for('change_password'))

        if len(new_pw) < 8:
            flash('新密码至少 8 位', 'danger')
            return redirect(url_for('change_password'))

        # 简单检查：不能与旧密码相同（可扩展更多规则）
        if bcrypt.check_password_hash(user['password_hash'], new_pw):
            flash('新密码不能与旧密码相同', 'danger')
            return redirect(url_for('change_password'))

        new_hash = bcrypt.generate_password_hash(new_pw).decode('utf-8')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE users SET password_hash = %s WHERE user_id = %s", (new_hash, user['user_id']))
        conn.commit()
        cur.close()
        conn.close()

        flash('密码修改成功，请重新登录', 'success')
        return redirect(url_for('logout'))

    return render_template('change_password.html', user=user)


# ────────────────────────────────────────────────
# 志愿者 - 浏览 & 筛选活动
# ────────────────────────────────────────────────
@app.route('/events')
@login_required
@role_required('volunteer')
def events():
    search_location = request.args.get('location', '')
    search_date = request.args.get('date', '')

    query = """
            SELECT e.*, \
                   u.full_name                                                       AS leader_name,
                   CASE WHEN er.registration_id IS NOT NULL THEN TRUE ELSE FALSE END AS registered
            FROM events e
                     JOIN users u ON e.event_leader_id = u.user_id
                     LEFT JOIN eventregistrations er ON e.event_id = er.event_id AND er.volunteer_id = %s
            WHERE e.event_date >= CURRENT_DATE \
            """
    params = [session['user_id']]

    if search_location:
        query += " AND e.location ILIKE %s"
        params.append(f"%{search_location}%")

    if search_date:
        query += " AND e.event_date = %s"
        params.append(search_date)

    query += " ORDER BY e.event_date, e.start_time"

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    events_list = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('events.html', events=events_list, search_location=search_location, search_date=search_date)


# ────────────────────────────────────────────────
# 志愿者 - 报名活动（含时间冲突检测）
# ────────────────────────────────────────────────
@app.route('/events/register/<int:event_id>', methods=['POST'])
@login_required
@role_required('volunteer')
def register_event(event_id):
    conn = get_db_connection()
    cur = conn.cursor()

    # 获取目标活动时间
    cur.execute("""
                SELECT event_date, start_time, duration
                FROM events
                WHERE event_id = %s
                  AND event_date >= CURRENT_DATE
                """, (event_id,))
    event = cur.fetchone()

    if not event:
        flash('活动不存在或已结束', 'danger')
        cur.close()
        conn.close()
        return redirect(url_for('events'))

    # 检查是否已报名
    cur.execute("SELECT 1 FROM eventregistrations WHERE event_id = %s AND volunteer_id = %s",
                (event_id, session['user_id']))
    if cur.fetchone():
        flash('您已报名此活动', 'info')
        cur.close()
        conn.close()
        return redirect(url_for('events'))

    # 检查时间冲突（同一时间段不能报多个活动）
    conflict_query = """
                     SELECT e.event_name
                     FROM events e
                              JOIN eventregistrations er ON e.event_id = er.event_id
                     WHERE er.volunteer_id = %s
                       AND e.event_date = %s
                       AND e.start_time < %s + INTERVAL '%s minutes'
                       AND e.start_time + INTERVAL '%s minutes' \
                         > %s \
                     """
    start_dt = datetime.combine(event['event_date'], event['start_time'])
    end_dt = start_dt + timedelta(minutes=event['duration'])

    cur.execute(conflict_query, (
        session['user_id'],
        event['event_date'],
        event['start_time'],
        event['duration'],
        event['duration'],
        event['start_time']
    ))
    conflict = cur.fetchone()

    if conflict:
        flash(f'时间冲突！您已报名 "{conflict["event_name"]}" 与此活动时间重叠', 'danger')
        cur.close()
        conn.close()
        return redirect(url_for('events'))

    # 报名
    cur.execute("""
                INSERT INTO eventregistrations (event_id, volunteer_id)
                VALUES (%s, %s)
                """, (event_id, session['user_id']))
    conn.commit()

    flash('报名成功！', 'success')
    cur.close()
    conn.close()
    return redirect(url_for('my_participation'))


# ────────────────────────────────────────────────
# 志愿者 - 我的参与历史
# ────────────────────────────────────────────────
@app.route('/my_participation')
@login_required
@role_required('volunteer')
def my_participation():
    conn = get_db_connection()
    cur = conn.cursor()

    # 未来活动
    cur.execute("""
                SELECT e.*, er.attendance, er.registered_at
                FROM events e
                         JOIN eventregistrations er ON e.event_id = er.event_id
                WHERE er.volunteer_id = %s
                  AND e.event_date >= CURRENT_DATE
                ORDER BY e.event_date, e.start_time
                """, (session['user_id'],))
    upcoming = cur.fetchall()

    # 历史活动 + 反馈状态
    cur.execute("""
                SELECT e.*, er.attendance, f.rating, f.comments
                FROM events e
                         JOIN eventregistrations er ON e.event_id = er.event_id
                         LEFT JOIN feedback f ON e.event_id = f.event_id AND f.volunteer_id = %s
                WHERE er.volunteer_id = %s
                  AND e.event_date < CURRENT_DATE
                ORDER BY e.event_date DESC
                """, (session['user_id'], session['user_id']))
    past = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('my_participation.html', upcoming=upcoming, past=past)


# ────────────────────────────────────────────────
# 志愿者 - 提交反馈（仅限已出席的过去活动）
# ────────────────────────────────────────────────
@app.route('/feedback/submit/<int:event_id>', methods=['GET', 'POST'])
@login_required
@role_required('volunteer')
def submit_feedback(event_id):
    conn = get_db_connection()
    cur = conn.cursor()

    # 验证：必须已出席且活动已结束
    cur.execute("""
                SELECT e.event_name, er.attendance, e.event_date
                FROM events e
                         JOIN eventregistrations er ON e.event_id = er.event_id
                WHERE er.volunteer_id = %s
                  AND e.event_id = %s
                """, (session['user_id'], event_id))
    data = cur.fetchone()

    if not data or data['attendance'] != 'attended' or data['event_date'] >= datetime.now().date():
        flash('无法提交反馈（活动未结束或未出席）', 'danger')
        cur.close()
        conn.close()
        return redirect(url_for('my_participation'))

    if request.method == 'POST':
        rating = int(request.form.get('rating'))
        comments = request.form.get('comments')

        try:
            cur.execute("""
                        INSERT INTO feedback (event_id, volunteer_id, rating, comments)
                        VALUES (%s, %s, %s, %s)
                        """, (event_id, session['user_id'], rating, comments))
            conn.commit()
            flash('反馈提交成功，感谢您的参与！', 'success')
        except psycopg2.IntegrityError:
            conn.rollback()
            flash('您已提交过反馈', 'info')

        cur.close()
        conn.close()
        return redirect(url_for('my_participation'))

    cur.close()
    conn.close()
    return render_template('submit_feedback.html', event_name=data['event_name'], event_id=event_id)


# ────────────────────────────────────────────────
# 活动负责人 - 创建活动
# ────────────────────────────────────────────────
@app.route('/leader/create_event', methods=['GET', 'POST'])
@login_required
@role_required('event_leader')
def create_event():
    if request.method == 'POST':
        event_name = request.form.get('event_name')
        location = request.form.get('location')
        event_date = request.form.get('event_date')
        start_time = request.form.get('start_time')
        duration = int(request.form.get('duration'))
        description = request.form.get('description')
        supplies = request.form.get('supplies')
        safety = request.form.get('safety_instructions')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO events (event_name, location, event_date, start_time, duration, description, supplies,
                                        safety_instructions, event_leader_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (event_name, location, event_date, start_time, duration, description, supplies, safety,
                          session['user_id']))
        conn.commit()
        cur.close()
        conn.close()

        flash('活动创建成功！', 'success')
        return redirect(url_for('leader_my_events'))

    return render_template('create_event.html')


# ────────────────────────────────────────────────
# 活动负责人 - 我的活动列表
# ────────────────────────────────────────────────
@app.route('/leader/my_events')
@login_required
@role_required('event_leader')
def leader_my_events():
    conn = get_db_connection()
    cur = conn.cursor()

    # 未来活动
    cur.execute("""
                SELECT e.*,
                       (SELECT COUNT(*) FROM eventregistrations WHERE event_id = e.event_id) AS volunteer_count
                FROM events e
                WHERE e.event_leader_id = %s
                  AND e.event_date >= CURRENT_DATE
                ORDER BY e.event_date, e.start_time
                """, (session['user_id'],))
    upcoming = cur.fetchall()

    # 历史活动
    cur.execute("""
                SELECT e.*,
                       (SELECT COUNT(*) FROM eventregistrations WHERE event_id = e.event_id) AS volunteer_count
                FROM events e
                WHERE e.event_leader_id = %s
                  AND e.event_date < CURRENT_DATE
                ORDER BY e.event_date DESC
                """, (session['user_id'],))
    past = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('leader_my_events.html', upcoming=upcoming, past=past)


# ────────────────────────────────────────────────
# 活动负责人 - 查看/管理单个活动
# ────────────────────────────────────────────────
@app.route('/leader/event/<int:event_id>')
@login_required
@role_required('event_leader')
def leader_event_detail(event_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT e.*, u.full_name AS leader_name
                FROM events e
                         JOIN users u ON e.event_leader_id = u.user_id
                WHERE e.event_id = %s
                  AND e.event_leader_id = %s
                """, (event_id, session['user_id']))
    event = cur.fetchone()

    if not event:
        flash('活动不存在或无权限', 'danger')
        cur.close()
        conn.close()
        return redirect(url_for('leader_my_events'))

    # 报名志愿者列表
    cur.execute("""
                SELECT u.*, er.attendance, er.registered_at
                FROM users u
                         JOIN eventregistrations er ON u.user_id = er.volunteer_id
                WHERE er.event_id = %s
                ORDER BY u.full_name
                """, (event_id,))
    volunteers = cur.fetchall()

    # 成果（如果已记录）
    cur.execute("SELECT * FROM eventoutcomes WHERE event_id = %s", (event_id,))
    outcome = cur.fetchone()

    # 反馈
    cur.execute("""
                SELECT f.*, u.full_name
                FROM feedback f
                         JOIN users u ON f.volunteer_id = u.user_id
                WHERE f.event_id = %s
                ORDER BY f.submitted_at DESC
                """, (event_id,))
    feedbacks = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('leader_event_detail.html', event=event, volunteers=volunteers, outcome=outcome,
                           feedbacks=feedbacks)


# ────────────────────────────────────────────────
# 活动负责人 - 记录活动成果
# ────────────────────────────────────────────────
@app.route('/leader/record_outcome/<int:event_id>', methods=['POST'])
@login_required
@role_required('event_leader')
def record_outcome(event_id):
    num_attendees = request.form.get('num_attendees', type=int, default=0)
    bags = request.form.get('bags_collected', type=int, default=0)
    recyclables = request.form.get('recyclables_sorted', type=int, default=0)
    achievements = request.form.get('other_achievements')

    conn = get_db_connection()
    cur = conn.cursor()

    # 只能记录自己的活动 & 活动已结束
    cur.execute("SELECT 1 FROM events WHERE event_id = %s AND event_leader_id = %s AND event_date < CURRENT_DATE",
                (event_id, session['user_id']))
    if not cur.fetchone():
        flash('无权限或活动尚未结束', 'danger')
        cur.close()
        conn.close()
        return redirect(url_for('leader_event_detail', event_id=event_id))

    cur.execute("""
                INSERT INTO eventoutcomes (event_id, num_attendees, bags_collected, recyclables_sorted,
                                           other_achievements)
                VALUES (%s, %s, %s, %s, %s) ON CONFLICT (event_id) DO
                UPDATE SET
                    num_attendees = EXCLUDED.num_attendees,
                    bags_collected = EXCLUDED.bags_collected,
                    recyclables_sorted = EXCLUDED.recyclables_sorted,
                    other_achievements = EXCLUDED.other_achievements,
                    recorded_at = CURRENT_TIMESTAMP
                """, (event_id, num_attendees, bags, recyclables, achievements))
    conn.commit()

    flash('活动成果已记录', 'success')
    cur.close()
    conn.close()
    return redirect(url_for('leader_event_detail', event_id=event_id))


# ────────────────────────────────────────────────
# admin - users
# ────────────────────────────────────────────────
@app.route('/admin/users')
@login_required
@role_required('admin')
def admin_users():
    search = request.args.get('search', '')

    query = "SELECT * FROM users WHERE 1=1"
    params = []

    if search:
        query += " AND (username ILIKE %s OR full_name ILIKE %s OR email ILIKE %s)"
        params.extend([f"%{search}%"] * 3)

    query += " ORDER BY role, full_name"

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    users_list = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('admin_users.html', users=users_list, search=search)


# ────────────────────────────────────────────────
# admin - toggle user status
# ────────────────────────────────────────────────
@app.route('/admin/toggle_user/<int:user_id>')
@login_required
@role_required('admin')
def toggle_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT status FROM users WHERE user_id = %s", (user_id,))
    user = cur.fetchone()

    if not user:
        flash('用户不存在', 'danger')
    else:
        new_status = 'inactive' if user['status'] == 'active' else 'active'
        cur.execute("UPDATE users SET status = %s WHERE user_id = %s", (new_status, user_id))
        conn.commit()
        flash(f'用户状态已切换为 {new_status}', 'success')

    cur.close()
    conn.close()
    return redirect(url_for('admin_users'))


# ────────────────────────────────────────────────
# admin - reports
# ────────────────────────────────────────────────
@app.route('/admin/reports')
@login_required
@role_required('admin')
def admin_reports():
    conn = get_db_connection()
    cur = conn.cursor()

    stats = {}

    # 用户统计
    cur.execute("SELECT role, COUNT(*) FROM users GROUP BY role")
    for row in cur.fetchall():
        stats[f"users_{row['role']}"] = row['count']

    cur.execute("SELECT COUNT(*) FROM users WHERE status = 'active'")
    stats['active_users'] = cur.fetchone()['count']

    # 活动统计
    cur.execute("SELECT COUNT(*) FROM events")
    stats['total_events'] = cur.fetchone()['count']

    cur.execute("SELECT COUNT(*) FROM events WHERE event_date >= CURRENT_DATE")
    stats['upcoming_events'] = cur.fetchone()['count']

    # 报名 & 反馈
    cur.execute("SELECT COUNT(*) FROM eventregistrations")
    stats['total_registrations'] = cur.fetchone()['count']

    cur.execute("SELECT COUNT(*) FROM feedback")
    stats['total_feedback'] = cur.fetchone()['count']

    cur.execute("SELECT AVG(rating) FROM feedback")
    avg = cur.fetchone()['avg']
    stats['avg_rating'] = round(avg, 2) if avg else 0

    # 成果汇总
    cur.execute("""
                SELECT SUM(bags_collected)     AS total_bags,
                       SUM(recyclables_sorted) AS total_recyclables,
                       SUM(num_attendees)      AS total_attendees
                FROM eventoutcomes
                """)
    outcomes = cur.fetchone()
    stats['total_bags'] = outcomes['total_bags'] or 0
    stats['total_recyclables'] = outcomes['total_recyclables'] or 0
    stats['total_attendees'] = outcomes['total_attendees'] or 0

    cur.close()
    conn.close()

    return render_template('admin_reports.html', stats=stats)


# ────────────────────────────────────────────────
# 静态文件服务（头像）
# ────────────────────────────────────────────────
@app.route('/profile_images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# ────────────────────────────────────────────────
# developer mode - run
# ────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
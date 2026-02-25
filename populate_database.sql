-- =============================================
-- COMP639 S1 2026 - EcoCleanUp Hub
-- Database Population Script (PostgreSQL)
-- Author: Chenghao Wu (1171540)
-- Run AFTER create_database.sql
-- =============================================

-- ======================
-- 1. USERS (27 users)
-- ======================
-- REPLACE EACH HASH WITH THE ONE FROM password_hash_generator.py
INSERT INTO users (username, password_hash, full_name, email, home_address, contact_number, profile_image, environmental_interests, role, status)
VALUES
-- Volunteers (1-20)
('volunteer01', '$2b$12$lsNpq1bdb.MDqnPA7q0XQOLt2OpoeKyrC3JxN1oBluhHId10hopFq', 'Emma Wilson', 'emma.w@example.nz', '12 River Road, Rolleston 7614', '021 123 4567', 'default_profile.jpg', 'beach cleanups, recycling, tree planting', 'volunteer', 'active'),
('volunteer02', '$2b$12$0zSStLJ.n6W9xGHG4kIhD.u3sNDc1YAN0zHtKDMLxdgBsm3EoCuim', 'Liam Thompson', 'liam.t@example.nz', '45 Main Street, Christchurch 8011', '027 234 5678', 'default_profile.jpg', 'recycling, litter picking', 'volunteer', 'active'),
('volunteer03', '$2b$12$gCGoyCpJSRJHUU952.4FxeYlvSGo837jCReSEyeO.oiZDHjjoUBSq', 'Olivia Chen', 'olivia.c@example.nz', '8 Ocean View, Sumner', '021 345 6789', 'default_profile.jpg', 'beach cleanups, marine life', 'volunteer', 'active'),
('volunteer04', '$2b$12$toTbLmr.Lqb9Y6WS/SfqxegSd18lRKFlp6DHkJ0zMs/2hLSN3DLcu', 'Noah Harris', 'noah.h@example.nz', '22 Park Lane, Rolleston', '027 456 7890', 'default_profile.jpg', 'tree planting, gardening', 'volunteer', 'active'),
('volunteer05', '$2b$12$mUK2qRfsCg6KBKpt6Yv8t.6q0vPU1NVft3whngyMbL7Y3juQigj82', 'Ava Martinez', 'ava.m@example.nz', '67 Lincoln Road, Christchurch', '021 567 8901', 'default_profile.jpg', 'recycling, composting', 'volunteer', 'active'),
('volunteer06', '$2b$12$j9QLtoWUVlksytOsopFKc.ksSd4kfGN.SzVqss.iFacaBk80c9fk2', 'Lucas Walker', 'lucas.w@example.nz', '3 Harbour View, Lyttelton', '027 678 9012', 'default_profile.jpg', 'beach cleanups, coastal protection', 'volunteer', 'active'),
('volunteer07', '$2b$12$nZ.yF1fiGAAfGywW1/3uoev5FZOEZL.f68jzd1.O74fBnCkNTdyg2', 'Isabella Lee', 'isabella.l@example.nz', '91 Halswell Road, Christchurch', '021 789 0123', 'default_profile.jpg', 'tree planting, native plants', 'volunteer', 'active'),
('volunteer08', '$2b$12$sZKAP.twSzwyvAOauyy.vOJ/vYItILgANKCuJoGoQXxHBDCM4PWny', 'Mason King', 'mason.k@example.nz', '14 Selwyn Street, Rolleston', '027 890 1234', 'default_profile.jpg', 'zero waste, recycling', 'volunteer', 'active'),
('volunteer09', '$2b$12$PWDy3U28t8qDfqW.YEzoJua2IEe.7zTAUBxXJwVesQ40cH3d9cRlG', 'Sophia Patel', 'sophia.p@example.nz', '55 Templeton Road, Christchurch', '021 901 2345', 'default_profile.jpg', 'beach cleanups, education', 'volunteer', 'active'),
('volunteer10', '$2b$12$Y9.C3sW8nAF0FsuTglNig.2IVOS6j/Y3RdJBhhpeJ.SeZEhDV.0ue', 'Ethan Nguyen', 'ethan.n@example.nz', '8 Brookside Lane, Rolleston', '027 012 3456', 'default_profile.jpg', 'litter picking, community events', 'volunteer', 'active'),
('volunteer11', '$2b$12$M8gdA1LoidQ54tXs2cejPOANfLm.rDsE1L4sZRjcXWeIjhjH26oxa', 'Mia Robinson', 'mia.r@example.nz', '33 Riccarton Road, Christchurch', '021 123 9876', 'default_profile.jpg', 'tree planting, wildlife', 'volunteer', 'active'),
('volunteer12', '$2b$12$a6IExi5m/BNCoZahkyALtu02xLgIAF3ybTXrh1skdsKARIPUE2KZu', 'James White', 'james.w@example.nz', '19 Lincoln University Campus', '027 234 8765', 'default_profile.jpg', 'recycling, campus cleanups', 'volunteer', 'active'),
('volunteer13', '$2b$12$ndwcTiswoGyfYBwyfOsji.Hpb0LPLofvjLsJRZmLCSw1WXNxgzCmS', 'Charlotte Scott', 'charlotte.s@example.nz', '42 Prebbleton Road, Rolleston', '021 345 7654', 'default_profile.jpg', 'beach cleanups, plastic free', 'volunteer', 'active'),
('volunteer14', '$2b$12$ccOjcnaps8mX8JekmNEsUeE4lGp9Z4e40Q5idRA39drRUbr9cfbGi', 'Benjamin Adams', 'benjamin.a@example.nz', '7 Ellesmere Road, Christchurch', '027 456 6543', 'default_profile.jpg', 'gardening, native restoration', 'volunteer', 'active'),
('volunteer15', '$2b$12$xeJ2Ufr5JRVYaUvfBjkPfeuSt/cD1xLqd565aIpCaQr0dyHsmJjcu', 'Amelia Clark', 'amelia.c@example.nz', '28 Halswell Junction, Rolleston', '021 567 5432', 'default_profile.jpg', 'community cleanups, education', 'volunteer', 'active'),
('volunteer16', '$2b$12$zo3Dv7d/ZrfUu8tJqvQ7KebaZ/AROKcqbVsgxz/Jx8ABDa7hUI68q', 'Daniel Lewis', 'daniel.l@example.nz', '61 Cashmere Road, Christchurch', '027 678 4321', 'default_profile.jpg', 'beach cleanups, marine', 'volunteer', 'active'),
('volunteer17', '$2b$12$eUab3/XWTmbzZ5NEUD0DSeeto/e1xQIix7/C79QSNLCobmYut4vQO', 'Harper Turner', 'harper.t@example.nz', '15 Dunns Crossing, Rolleston', '021 789 3210', 'default_profile.jpg', 'tree planting, sustainability', 'volunteer', 'active'),
('volunteer18', '$2b$12$uf3eoggfNRz2dH0I4qdDg.4UuJg1fCAIDgNR0ghFUqfX/D5XGWYd.', 'Alexander Hall', 'alex.h@example.nz', '9 Yaldhurst Road, Christchurch', '027 890 2109', 'default_profile.jpg', 'litter removal, parks', 'volunteer', 'active'),
('volunteer19', '$2b$12$6HaljTI2SEdCQ4qbVH0rZ.8qFEx/CAnoPPzRKS6DueWQhV8IsIRKG', 'Evelyn Young', 'evelyn.y@example.nz', '3 Goulds Road, Rolleston', '021 901 1098', 'default_profile.jpg', 'recycling, zero waste', 'volunteer', 'active'),
('volunteer20', '$2b$12$58w3sWExzrBp04g.mLa1qeQrh.cAujvT0uWjn3598lE.1FGR6/KJW', 'Logan Wright', 'logan.w@example.nz', '82 Main South Road, Christchurch', '027 012 0987', 'default_profile.jpg', 'all environmental causes', 'volunteer', 'active'),

-- Event Leaders (21-25)
('leader01', '$2b$12$EhcJemko5W0.qhPzK7.n9.7q6NVHYkeM6EAOqqnZy4y3DQ2fNDjHO', 'Sarah Mitchell', 'sarah.m@example.nz', '10 Cathedral Square, Christchurch', '021 111 2222', 'default_profile.jpg', 'organising cleanups', 'event_leader', 'active'),
('leader02', '$2b$12$RVpc0V/7h7pbfAF83GKyhepHBps8ex6j7ARBRJvxJnPpY2y4KNOri', 'Jacob Green', 'jacob.g@example.nz', '5 Market Place, Rolleston', '027 333 4444', 'default_profile.jpg', 'coastal events', 'event_leader', 'active'),
('leader03', '$2b$12$FLHHV8DedjnfQzBnRveiQe2hqNvEWBJdFTXRkFEesgSI10M4F7wIe', 'Zoe Campbell', 'zoe.c@example.nz', '22 Oxford Terrace, Christchurch', '021 555 6666', 'default_profile.jpg', 'community events', 'event_leader', 'active'),
('leader04', '$2b$12$1EvsmHuKpgL5eizBxLS3EOiqaK2SWBNBqIQl99Hdc/Idx3CQ5AsbK', 'Henry Baker', 'henry.b@example.nz', '7 Lincoln Road, Rolleston', '027 777 8888', 'default_profile.jpg', 'park restoration', 'event_leader', 'active'),
('leader05', '$2b$12$Kg.SUD0SS7kK74pkOnscd.hx4O.QjZVYwF0kDJMOtGiw2q2h44IBu', 'Lily Evans', 'lily.e@example.nz', '19 Victoria Street, Christchurch', '021 999 0000', 'default_profile.jpg', 'education & cleanups', 'event_leader', 'active'),

-- Administrators (26-27)
('admin01', '$2b$12$Adny2PZL..Fh8wNVozgokuCNZVQLOjoSC.ShMFHGMfHgVmW7KWSDG', 'Admin One', 'admin1@ecocleanup.nz', 'University of Canterbury', '021 000 1111', 'default_profile.jpg', 'system management', 'admin', 'active'),
('admin02', '$2b$12$/3Od.i2uurQWcX3/kcyrdedzTzoTiLRFtjOwyGxUN99hRmm7KXJKm', 'Admin Two', 'admin2@ecocleanup.nz', 'Rolleston Town Hall', '027 222 3333', 'default_profile.jpg', 'platform oversight', 'admin', 'active');

-- ======================
-- 2. EVENTS (25 events)
-- ======================
INSERT INTO events (event_name, location, event_date, start_time, duration, description, supplies, safety_instructions, event_leader_id)
VALUES
('Sumner Beach Clean-Up', 'Sumner Beach, Christchurch', '2026-03-15', '09:00:00', 180, 'Monthly beach clean-up focusing on plastic pollution.', 'Gloves, bags, litter pickers', 'Wear closed shoes, sun protection, no swimming', 21),
('Rolleston Park Restoration', 'Rolleston Central Park', '2026-03-22', '10:00:00', 240, 'Tree planting and weed removal day.', 'Spades, gloves, seedlings', 'Stay on paths, drink water', 22),
('Lyttelton Harbour Litter Pick', 'Lyttelton Harbour', '2026-03-28', '08:30:00', 150, 'Harbour foreshore clean-up.', 'Buckets, gloves', 'Tide awareness, life jackets for water edge', 23),
('Halswell River Clean-Up', 'Halswell River Track', '2026-04-05', '09:30:00', 210, 'Remove rubbish from riverbanks.', 'Bags, pickers', 'Watch for slippery banks', 21),
('Lincoln University Campus Clean', 'Lincoln University', '2026-04-12', '11:00:00', 120, 'Student-led campus tidy-up.', 'Gloves, bags', 'Respect university property', 24),
('Banks Peninsula Track Clean', 'Banks Peninsula Track start', '2026-04-19', '08:00:00', 300, 'Scenic track litter removal.', 'Backpacks, gloves', 'Bring water and snacks', 22),
('Christchurch Botanic Gardens Weed Pull', 'Botanic Gardens', '2026-04-26', '10:00:00', 180, 'Volunteer weed removal session.', 'Gloves, tools provided', 'No digging without permission', 25),
('Avon River Rubbish Removal', 'Avon River, Hagley Park', '2026-05-03', '09:00:00', 240, 'River and park clean-up.', 'Waders optional, bags', 'Slippery areas', 23),
('Prebbleton Community Clean', 'Prebbleton Village Green', '2026-05-10', '10:30:00', 150, 'Local village tidy-up.', 'All supplies provided', 'Family friendly', 24),
('New Brighton Beach Clean', 'New Brighton Beach', '2026-05-17', '09:00:00', 180, 'Popular beach clean-up.', 'Gloves, bags', 'High tide awareness', 21),
('Rolleston School Eco Day', 'Rolleston School Grounds', '2026-05-24', '13:00:00', 120, 'Kids and parents clean-up.', 'Gloves, small bags', 'Supervise children', 22),
('Port Hills Track Clean', 'Port Hills Summit Road', '2026-05-31', '08:30:00', 210, 'Track maintenance clean-up.', 'Gloves, bags', 'Steep terrain', 25),
('Riccarton Bush Litter Pick', 'Riccarton Bush', '2026-06-07', '10:00:00', 150, 'Native bush protection clean.', 'Gloves only', 'Stay on paths', 23),
('Selwyn River Clean-Up', 'Selwyn River, near Rolleston', '2026-06-14', '09:30:00', 240, 'Riverbank rubbish removal.', 'Bags, gloves', 'River flow awareness', 24),
('Cashmere Hills Park Clean', 'Cashmere Hills', '2026-06-21', '10:00:00', 180, 'Hill park tidy-up.', 'Gloves, bags', 'Steep slopes', 21),
('Yaldhurst Road Community Clean', 'Yaldhurst Road, Christchurch', '2026-06-28', '09:00:00', 150, 'Roadside litter pick.', 'High-vis vests', 'Traffic safety', 22),
('Lincoln University Farm Clean', 'Lincoln University Farm', '2026-07-05', '11:00:00', 180, 'Farm perimeter clean-up.', 'Gloves, bags', 'Respect animals', 25),
('Hagley Park Big Clean', 'Hagley Park', '2026-07-12', '10:00:00', 240, 'Large park clean-up event.', 'All supplies', 'Family friendly', 23),
('Sumner Headland Track Clean', 'Sumner Headland', '2026-07-19', '08:30:00', 210, 'Clifftop track maintenance.', 'Gloves, bags', 'Cliff safety', 24),
('Rolleston Youth Eco Day', 'Rolleston Youth Centre', '2026-07-26', '13:00:00', 120, 'Youth-led clean-up.', 'Gloves, fun activities', 'Supervision required', 21),
('Templeton Community Clean', 'Templeton Village', '2026-08-02', '10:00:00', 180, 'Village green clean-up.', 'Supplies provided', 'All ages welcome', 22),
('Christchurch City Cycleway Clean', 'Cycleways across city', '2026-08-09', '09:00:00', 150, 'Cycle path litter removal.', 'Bags, gloves', 'Watch for cyclists', 25),
('Banks Peninsula Farm Clean', 'Private farm, Banks Peninsula', '2026-08-16', '10:00:00', 240, 'Farm and track clean-up.', 'Gloves, bags', 'Farm rules', 23),
('Avon-Heathcote Estuary Clean', 'Estuary Reserve', '2026-08-23', '09:30:00', 180, 'Estuary protection day.', 'Waders optional', 'Tide times', 24),
('Final Big Clean 2026', 'Multiple locations', '2026-08-30', '08:00:00', 300, 'End of season mega clean-up.', 'All supplies', 'Safety briefing', 21);

-- ======================
-- 3. EVENT REGISTRATIONS (30 registrations)
-- ======================
INSERT INTO eventregistrations (event_id, volunteer_id, registered_at, attendance)
VALUES
(1,1,NOW()-INTERVAL'5 days','pending'), (1,2,NOW()-INTERVAL'4 days','pending'),
(2,3,NOW()-INTERVAL'6 days','pending'), (2,4,NOW()-INTERVAL'3 days','pending'),
(3,5,NOW()-INTERVAL'7 days','pending'), (3,6,NOW()-INTERVAL'2 days','pending'),
(4,7,NOW()-INTERVAL'8 days','pending'), (4,8,NOW()-INTERVAL'1 day','pending'),
(5,9,NOW()-INTERVAL'9 days','pending'), (5,10,NOW()-INTERVAL'5 days','pending'),
(6,11,NOW()-INTERVAL'10 days','pending'), (6,12,NOW()-INTERVAL'4 days','pending'),
(7,13,NOW()-INTERVAL'11 days','pending'), (7,14,NOW()-INTERVAL'3 days','pending'),
(8,15,NOW()-INTERVAL'12 days','pending'), (8,16,NOW()-INTERVAL'2 days','pending'),
(9,17,NOW()-INTERVAL'13 days','pending'), (9,18,NOW()-INTERVAL'1 day','pending'),
(10,19,NOW()-INTERVAL'14 days','pending'), (10,20,NOW()-INTERVAL'6 days','pending'),
(1,11,NOW()-INTERVAL'8 days','pending'), (2,12,NOW()-INTERVAL'7 days','pending'),
(11,1,NOW()-INTERVAL'9 days','pending'), (12,2,NOW()-INTERVAL'5 days','pending'),
(13,3,NOW()-INTERVAL'10 days','pending'), (14,4,NOW()-INTERVAL'4 days','pending'),
(15,5,NOW()-INTERVAL'11 days','pending'), (16,6,NOW()-INTERVAL'3 days','pending'),
(17,7,NOW()-INTERVAL'12 days','pending'), (18,8,NOW()-INTERVAL'2 days','pending');

-- ======================
-- 4. EVENT OUTCOMES (for 15 past/recent events)
-- ======================
INSERT INTO eventoutcomes (event_id, num_attendees, bags_collected, recyclables_sorted, other_achievements)
VALUES
(1,18,42,15,'Lots of microplastics removed'),
(2,22,31,28,'Planted 45 native trees'),
(3,14,28,19,'Removed fishing nets'),
(4,19,35,22,'Cleared invasive weeds'),
(5,25,18,12,'Student turnout excellent'),
(6,16,29,17,'Beautiful views enjoyed'),
(7,20,24,30,'Rare orchids protected'),
(8,17,33,21,'River water quality improved'),
(9,12,15,8,'Community spirit high'),
(10,21,38,25,'Record bags collected'),
(11,30,45,32,'Kids learned a lot'),
(12,13,19,14,'Track now safer'),
(13,18,26,16,'Native bush restored'),
(14,15,22,18,'River clearer than ever'),
(15,23,37,29,'Hill views stunning');

-- ======================
-- 5. FEEDBACK (12 sample feedbacks)
-- ======================
INSERT INTO feedback (event_id, volunteer_id, rating, comments, submitted_at)
VALUES
(1,1,5,'Amazing turnout and beautiful day!', NOW()-INTERVAL'3 days'),
(1,2,4,'Great organisation, a bit windy but fun!', NOW()-INTERVAL'3 days'),
(2,3,5,'Loved planting trees! Will come again.', NOW()-INTERVAL'4 days'),
(3,5,4,'Harbour was stunning, learned a lot.', NOW()-INTERVAL'5 days'),
(4,7,5,'Very well organised, felt safe.', NOW()-INTERVAL'6 days'),
(5,9,5,'Super fun with students!', NOW()-INTERVAL'7 days'),
(6,11,4,'Great views but steep in places.', NOW()-INTERVAL'8 days'),
(7,13,5,'Best event yet!', NOW()-INTERVAL'9 days'),
(8,15,5,'River looks so much better.', NOW()-INTERVAL'10 days'),
(10,19,4,'Huge turnout, very satisfying.', NOW()-INTERVAL'11 days'),
(11,1,5,'Kids had a blast!', NOW()-INTERVAL'12 days'),
(12,2,5,'Port Hills never disappoints.', NOW()-INTERVAL'13 days');

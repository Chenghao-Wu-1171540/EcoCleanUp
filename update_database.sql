CREATE TYPE event_status_enum AS ENUM ('upcoming', 'ongoing', 'completed', 'cancelled');

CREATE TYPE event_type_enum AS ENUM (
    'Beach Clean-up', 'River Clean-up', 'Park Restoration',
    'Track Maintenance', 'Community Event', 'Campus Clean', 'Other'
);

ALTER TABLE events
    ADD COLUMN event_type event_type_enum
    NOT NULL
    DEFAULT 'Other';

ALTER TABLE events
    ADD COLUMN IF NOT EXISTS event_status event_status_enum
    NOT NULL DEFAULT 'upcoming';


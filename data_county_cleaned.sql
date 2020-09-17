SET ROLE ckallaya;
CREATE SCHEMA IF NOT EXISTS socioecon_schema;
DROP TABLE IF EXISTS socioecon_schema.socioecon_table1;
CREATE TABLE socioecon_schema.socioecon_table1 (
        a DECIMAL NOT NULL,
        detail VARCHAR NOT NULL,
        unemploy DECIMAL NOT NULL,
        income DECIMAL NOT NULL,
        white DECIMAL NOT NULL,
        black DECIMAL NOT NULL,
        indian_alaskan DECIMAL NOT NULL,
        asian DECIMAL NOT NULL,
        population DECIMAL NOT NULL,
        male DECIMAL NOT NULL,
        female DECIMAL NOT NULL,
        high_school DECIMAL NOT NULL,
        ged DECIMAL NOT NULL,
        college_less_1yr DECIMAL NOT NULL,
        college_more_1yr DECIMAL NOT NULL,
        associate DECIMAL NOT NULL,
        bachelor DECIMAL NOT NULL,
        master DECIMAL NOT NULL,
        professional DECIMAL NOT NULL,
        doctorate DECIMAL NOT NULL,
        block_group DECIMAL NOT NULL,
        tract DECIMAL NOT NULL,
        county_code DECIMAL NOT NULL,
        state_code DECIMAL NOT NULL
);

\copy socioecon_schema.socioecon_table1 from 'data_county_cleaned.csv' with csv header;




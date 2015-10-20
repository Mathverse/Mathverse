-- [LEFT BLANK]

-- SEARCH_ORGS function
DROP FUNCTION IF EXISTS search_orgs(character varying);

CREATE OR REPLACE FUNCTION search_orgs(org_name_search_str varchar)
  RETURNS TABLE(id int, name varchar)
  LANGUAGE plpgsql
  AS
  $$
  DECLARE
    org_name_search_str_with_wildcards varchar;
  BEGIN
    org_name_search_str_with_wildcards := '%' || org_name_search_str || '%';

    RETURN QUERY
    SELECT
      *
    FROM
      "ChicagoBoothAnalytics_app_org"
    WHERE
      "ChicagoBoothAnalytics_app_org".name LIKE org_name_search_str_with_wildcards
    ORDER BY
      "ChicagoBoothAnalytics_app_org".name;
  END
  $$;


-- QUERY_PERSONS function
DROP FUNCTION IF EXISTS search_persons(character varying);

CREATE OR REPLACE FUNCTION search_persons(person_name_search_str varchar)
  RETURNS TABLE(id int, first_name varchar, last_name varchar, gender boolean, first_name_alias varchar)
  LANGUAGE plpgsql
  AS
  $$
  DECLARE
    person_name_search_str_with_wildcards varchar;
  BEGIN
    person_name_search_str_with_wildcards := '%' || person_name_search_str || '%';

    RETURN QUERY
    SELECT
      *
    FROM
      "ChicagoBoothAnalytics_app_person"
    WHERE
      "ChicagoBoothAnalytics_app_person".last_name LIKE person_name_search_str_with_wildcards
    ORDER BY
      "ChicagoBoothAnalytics_app_person".last_name;
  END
  $$
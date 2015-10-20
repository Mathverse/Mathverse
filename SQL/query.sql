-- [LEFT BLANK]
\i functions.sql


-------------------------------------------
-- *** ORIGINAL TABLES FROM DATABASE *** --
-------------------------------------------


-- BusinessSector table
drop table if exists BusinessSector;
select
  id,
  name
into
  BusinessSector
from
  "ChicagoBoothAnalytics_app_businesssector"
order by
  name;


-- GeofRegion table
drop table if exists GeogRegion;
select
  id,
  name
into
  GeogRegion
from
  "ChicagoBoothAnalytics_app_geogregion"
order by
  name;


-- Org table
drop table if exists Org;
select
  id,
  name
into
  Org
from
  search_orgs('')
order by
  name;


-- Org_BusinessSector table
drop table if exists Org_BusinessSector_m2m_ids;
select
  id,
  org_id,
  businesssector_id as business_sector_id
into
  Org_BusinessSector_m2m_ids
from
  "ChicagoBoothAnalytics_app_org_business_sectors";

drop table if exists Org_BusinessSector;
select
  Org_BusinessSector_m2m_ids.id as id,
  Org_BusinessSector_m2m_ids.org_id as org_id,
  Org_BusinessSector_m2m_ids.business_sector_id as business_sector_id,
  Org.name as org,
  BusinessSector.name as business_sector
into
  Org_BusinessSector
from
  Org_BusinessSector_m2m_ids
    left join Org on Org_BusinessSector_m2m_ids.org_id = Org.id
    left join BusinessSector on Org_BusinessSector_m2m_ids.business_sector_id = BusinessSector.id;


-- Org_GeogRegion table
drop table if exists Org_GeogRegion_m2m_ids;
select
  id,
  org_id,
  geogregion_id as geog_region_id
into
  Org_GeogRegion_m2m_ids
from
  "ChicagoBoothAnalytics_app_org_geog_regions";

drop table if exists Org_GeogRegion;
select
  Org_GeogRegion_m2m_ids.id as id,
  Org_GeogRegion_m2m_ids.org_id as org_id,
  Org_GeogRegion_m2m_ids.geog_region_id as geog_region_id,
  Org.name as org,
  GeogRegion.name as geog_region
into
  Org_GeogRegion
from
  Org_GeogRegion_m2m_ids
    left join Org on Org_GeogRegion_m2m_ids.org_id = Org.id
    left join GeogRegion on Org_GeogRegion_m2m_ids.geog_region_id = GeogRegion.id;


-- Person table
drop table if exists Person;
select
  id,
  coalesce(nullif(first_name_alias, ''), first_name) || ' ' || upper(last_name) as name,
  last_name,
  first_name,
  first_name_alias,
  gender
into
  Person
from
  search_persons('')
order by
  last_name;


-- RoleLevel table
drop table if exists RoleLevel;
select
  id,
  level,
  level_number_from_high_to_low
into
  RoleLevel
from
  "ChicagoBoothAnalytics_app_rolelevel"
order by
  level_number_from_high_to_low;


-- Role table
drop table if exists Role___temp;
select
  *
into
  Role___temp
from
  "ChicagoBoothAnalytics_app_role";

drop table if exists Role;
select
  Role___temp.id as id,
  Role___temp.title || ' [' || RoleLevel.level || '-level]' as title,
  RoleLevel.level_number_from_high_to_low as level_number_from_high_to_low
into
  Role
from
  Role___temp
    join RoleLevel on Role___temp.level_id = RoleLevel.id
order by
  RoleLevel.level_number_from_high_to_low,
  Role___temp.title;


-- CareerOpportunity_GeogRegion table
drop table if exists CareerOpportunity_GeogRegion___temp;
select
  careeropportunity_id as career_opportunity_id,
  geogregion_id as geog_region_id
into 
  CareerOpportunity_GeogRegion___temp
from
  "ChicagoBoothAnalytics_app_careeropportunity_geog_regions";

drop table if exists CareerOpportunity_GeogRegion;
select
  CareerOpportunity_GeogRegion___temp.career_opportunity_id as career_opportunity_id,
  GeogRegion.name as geog_region
into 
  CareerOpportunity_GeogRegion
from
  CareerOpportunity_GeogRegion___temp
    left join GeogRegion on CareerOpportunity_GeogRegion___temp.geog_region_id = GeogRegion.id;


-- CareerOpportunity table
drop table if exists CareerOpportunity___temp;
select
  id,
  org_id,
  role_id,
  active as open,
  posting_date,
  url
into
  CareerOpportunity___temp
from
  "ChicagoBoothAnalytics_app_careeropportunity"
order by
  not active;

drop table if exists CareerOpportunity;
select 
  CareerOpportunity___temp.id as id,
  Org.name as org,
  Role.title as role,
  Role.level_number_from_high_to_low as level_number_from_high_to_low,
  CareerOpportunity_GeogRegion.geog_region as geog_region,
  CareerOpportunity___temp.open as open,
  CareerOpportunity___temp.posting_date as posting_date,
  CareerOpportunity___temp.url as url
into
  CareerOpportunity
from
  CareerOpportunity___temp
    left join Org on CareerOpportunity___temp.org_id = Org.id
    left join Role on CareerOpportunity___temp.role_id = Role.id
    left join CareerOpportunity_GeogRegion on CareerOpportunity___temp.id = CareerOpportunity_GeogRegion.career_opportunity_id
order by
  not CareerOpportunity___temp.open,
  Org.name,
  Role.level_number_from_high_to_low,
  Role.title,
  CareerOpportunity_GeogRegion.geog_region;


-- FactType table
drop table if exists FactType;
select
  id,
  label
into
  FactType
from
  "ChicagoBoothAnalytics_app_facttype"
order by
  label;


-- OrgFact table
drop table if exists OrgFact___temp;
select
  id,
  org_id,
  fact_type_id,
  fact
into
  OrgFact___temp
from
  "ChicagoBoothAnalytics_app_orgfact";

drop table if exists OrgFact;
select
  OrgFact___temp.id as id,
  OrgFact___temp.org_id as org_id,
  OrgFact___temp.fact_type_id as fact_type_id,
  Org.name as org,
  FactType.label as fact_type,
  OrgFact___temp.fact as fact
into
  OrgFact
from
  OrgFact___temp
    left join Org on OrgFact___temp.org_id = Org.id
    left join FactType on OrgFact___temp.fact_type_id = FactType.id;
    

----------------------------
-- *** DERIVED TABLES *** --
----------------------------


-- FactType_website table
drop table if exists FactType_website;
select
  id,
  label
into
  FactType_website
from
  "ChicagoBoothAnalytics_app_facttype"
where
  label = 'website';

-- OrgWebsites table
drop table if exists OrgFact_website;
select
  OrgFact.org_id as org_id,
  OrgFact.fact as website
into
  OrgFact_website
from
  OrgFact
    inner join FactType_website on OrgFact.fact_type_id = FactType_website.id;


-- Org_OpenCareerOpportunities
drop table if exists OrgNbOpenCareerOpportunities;
select
  org_id, count(*) as nb_open_career_opportunities
into
  OrgNbOpenCareerOpportunities
from
  "ChicagoBoothAnalytics_app_careeropportunity"
where
  active = true
group by
  org_id;


-- OrgOverview table
drop table if exists OrgOverview;
select
  Org.id as id,
  Org.name as name,
  string_agg(OrgFact_website.website, ' | ') as websites,
  string_agg(Org_BusinessSector.business_sector, ' | ') as business_sectors,
  string_agg(Org_GeogRegion.geog_region, ' | ') as geog_regions,
  OrgNbOpenCareerOpportunities.nb_open_career_opportunities as nb_open_career_opportunities
into
  OrgOverview
from
  Org
    left join OrgFact_website on Org.id = OrgFact_website.org_id
    left join Org_BusinessSector on Org.id = Org_BusinessSector.org_id
    left join Org_GeogRegion on Org.id = Org_GeogRegion.org_id
    left join OrgNbOpenCareerOpportunities on org.id = OrgNbOpenCareerOpportunities.org_id
group by
  Org.id,
  Org.name,
  OrgNbOpenCareerOpportunities.nb_open_career_opportunities
order by
  Org.name;


-- CareerOpportunityList table
drop table if exists CareerOpportunityList;
select
  id,
  org,
  role,
  level_number_from_high_to_low,
  string_agg(geog_region, ' | ') as geog_regions,
  open,
  posting_date,
  url
into
  CareerOpportunityList
from
  CareerOpportunity
group by
  id,
  org,
  role,
  level_number_from_high_to_low,
  open,
  posting_date,
  url;
--order by
 -- not CareerOpportunity.open,
 -- CareerOpportunity.org,
 -- CareerOpportunity.level_number_from_high_to_low,
 -- geog_regions;




-- save results to .CSV files
-- NOTE: a '\copy ...' statement must stay on 1 line
\copy BusinessSector to 'zzz_BusinessSector.csv' with delimiter ',' csv header;
\copy GeogRegion to 'zzz_GeogRegion.csv' with delimiter ',' csv header;
\copy Org to 'zzz_Org.csv' with delimiter ',' csv header;
\copy Org_BusinessSector to 'zzz_Org_BusinessSector.csv' with delimiter ',' csv header;
\copy Org_GeogRegion to 'zzz_Org_GeogRegion.csv' with delimiter ',' csv header;
\copy Person to 'zzz_Person.csv' with delimiter ',' csv header;
\copy RoleLevel to 'zzz_RoleLevel.csv' with delimiter ',' csv header;
\copy Role to 'zzz_Role.csv' with delimiter ',' csv header;
\copy CareerOpportunity to 'zzz_CareerOpportunity.csv' with delimiter ',' csv header;
\copy CareerOpportunity_GeogRegion to 'zzz_CareerOpportunity_GeogRegion.csv' with delimiter ',' csv header;
\copy FactType to 'zzz_FactType.csv' with delimiter ',' csv header;
\copy OrgFact to 'zzz_OrgFact.csv' with delimiter ',' csv header;
\copy OrgOverview to 'tbl_OrgOverview.csv' with delimiter ',' csv header;
\copy CareerOpportunityList to 'tbl_CareerOpportunity.csv' with delimiter ',' csv header;

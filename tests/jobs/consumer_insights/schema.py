from pyspark.sql.types import StructField, StructType, LongType, StringType, ShortType, TimestampType

from shared.constants import PiiHashingColumnNames, InputColumnNames, ConsumerViewSchema, LeadEventSchema, \
    PublisherPermissions


def expected_pii_hashing_schema():
    return StructType(
        [StructField(PiiHashingColumnNames.RECORD_ID, LongType()),
         StructField(PiiHashingColumnNames.INPUT_ID_RAW, StringType()),
         StructField(PiiHashingColumnNames.INPUT_ID, StringType()),
         StructField(PiiHashingColumnNames.INPUT_ID_TYPE, StringType())])


def expected_pii_hashing_consumer_view_transformed_schema():
    return StructType(
        [StructField(PiiHashingColumnNames.RECORD_ID, LongType()),
         StructField(ConsumerViewSchema.CLUSTER_ID, LongType())])


def expected_consumer_insights_no_lead_info_schema():
    return StructType(
        [StructField(InputColumnNames.RECORD_ID, LongType()),
         StructField(InputColumnNames.INPUT_ID, StringType())])


def expected_consumer_insights_result_schema():
    return StructType(
        [StructField(InputColumnNames.RECORD_ID, LongType()),
         StructField(InputColumnNames.INPUT_ID, StringType()),
         StructField(LeadEventSchema.CREATION_TS, StringType()),
         StructField(LeadEventSchema.CAMPAIGN_KEY, StringType())])


def consumer_view_schema():
    return StructType(
        [StructField(ConsumerViewSchema.NODE_TYPE_CD, StringType()),
         StructField(ConsumerViewSchema.NODE_VALUE, StringType()),
         StructField(ConsumerViewSchema.CLUSTER_ID, LongType())])


def lead_id_schema():
    return StructType(
        [StructField(InputColumnNames.RECORD_ID, LongType()),
         StructField(InputColumnNames.INPUT_ID, StringType())])


def lead_event_schema():
    return StructType(
        [StructField(InputColumnNames.LEAD_ID, StringType()),
         StructField(LeadEventSchema.CREATION_TS, StringType()),
         StructField(LeadEventSchema.CAMPAIGN_KEY, StringType())])


def v_campaign_opt_in_state_schema():
    return StructType(
        [StructField(PublisherPermissions.CAMPAIGN_KEY, StringType()),
         StructField(PublisherPermissions.APPLICATION_KEY, LongType()),
         StructField(PublisherPermissions.OPT_IN_IND, ShortType()),
         StructField(PublisherPermissions.INSERT_TS, TimestampType()),
         StructField(PublisherPermissions.INSERT_JOB_RUN_ID, LongType())])


def expected_publisher_permissions_result_schema():
    return StructType(
        [StructField(InputColumnNames.RECORD_ID, LongType()),
         StructField(InputColumnNames.INPUT_ID, StringType()),
         StructField(LeadEventSchema.CREATION_TS, StringType())])


def filtered_campaign_opt_in_view():
    return StructType([StructField(PublisherPermissions.VIEW_CAMPAIGN_KEY, StringType())])
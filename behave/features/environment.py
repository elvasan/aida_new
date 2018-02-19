from datetime import datetime

import json
import os
import pytz

from utils.aws_utils import AWSUtils


#    Before any test run, process the command line options
#    -D env=    use this environment from config.json and ~/.aws/config
#    -D upload= use this timestamp for the upload file (but do not upload one)
#                the format is 'yyyymmdd_HHMM' in the UTC timezone
def before_all(context):
    # Get the test environment, defauilt to 'qa'
    context.envName = 'dev'
    if context.config.userdata.get('env') is not None:
        context.envName = context.config.userdata.get('env')

    # See if data/tmp should be cleaned up
    context.do_cleanup = True
    if context.config.userdata.get('cleanup') is not None:
        if context.config.userdata.get('cleanup').lower()[0] == 'f':
            context.do_cleanup = False

    # See if upload should be done
    context.uploadTimestamp = None
    if context.config.userdata.get('upload') is not None:
        context.uploadTimestamp = pytz.utc.localize(datetime.strptime(
            context.config.userdata.get('upload') + " UTC",
            '%Y%m%d_%H%M %Z'))

    # Get the config file path and make sure it exists
    context.scriptDir = os.path.dirname(__file__)
    context.configFile = os.path.join(context.scriptDir, '../config.json')
    assert os.path.exists(context.configFile)

    # read the config and set up the context
    config = json.load(open(context.configFile))

    # NEEDED FOR AWS_UTILS.PY
    context.appName = config[context.envName]["appName"]
    context.region = config[context.envName]["region"]
    context.bucketName = '{}-{}-{}'.format(context.envName, context.region, context.appName)

    # Define the input, temp and expected file directories
    # Create the tmp directory if it's not there
    context.inputDataDir = os.path.join(context.scriptDir, "../data/input_data")
    context.expectedDataDir = os.path.join(context.scriptDir, "../data/expected_data")
    context.tempDataDir = os.path.join(context.scriptDir, '../data/tmp')

    # Connect to AWS.
    # This will prompt for your MFA code
    context.aws = AWSUtils.get_instance(context)

    pass

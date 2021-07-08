"""
Copyright 2021 Janrey "CodexLink" Licas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Classifications of constants of any kind. (limiters, choices, etc.) | constants.py
# Version dev.0.06232021


if __name__ == "__main__":
    from .exceptions import IsolatedExecNotAllowed

    raise IsolatedExecNotAllowed

else:
    from typing import Any, Final, List
    from time import strftime
    from discord import Intents
    from datetime import datetime
    # # Badge Generator Constants

    BADGE_BASE_URL: Final[str] = "https://badgen.net"
    BADGE_URI: Final[str] = BADGE_BASE_URL + "/badge/%s/%s/%s"
    BADGE_DEFAULT_SUBJECT: Final[str] = "Rich Presence" # todo: Add this as one of the variables that can be overriden.
    BADGE_DEFAULT_SUBJECT_BG_COLOR: Final[str] = "black"
    BADGE_DEFAULT_STATUS: Final[str] = "%s %s"
    BADGE_DEFAULT_STATUS_BG_COLOR: Final[str] = "red"
    BADGE_DEFAULT_STATUS_SEP_CHAR: Final[str] = "|"
    BADGE_ICON: Final[str] = "discord"

    # # Classified Arguments Information
    ARG_CONSTANTS: Final[dict[str, str]] = {  # Cannot evaluate less.
        "ENTRY_PARSER_DESC": "An application that runs under workflow to evaluate User's Discord Activity Presence to Displayable Badge for their README.md.",
        "ENTRY_PARSER_EPILOG": "The use of arguments are intended for debugging purposes only. Please be careful.",
        "HELP_DESC_DRY_RUN": "Runs the whole script without commiting changes to external involved factors (ie. README.md)",
        "HELP_DESC_LOG_TO_CONSOLE": "Prints the log output to the console, whenever the case.",
        "HELP_DESC_NO_ALERT_USR": "Does not alert the user / developer from the possible crashes through Direct Messages (this also invokes the do-not-send logs.)",
        "HELP_DESC_NO_LOG_TO_FILE": "Disables logging to file but does not surpress outputting logs to console, if specified.",
        "HELP_DESC_RUNNING_LOCALLY": "Allows the script from loading .env. This can raise or terminate if '.env' cannot be found.",
        "HELP_DESC_VERBOSE_CLIENT": "Allows Discord Client API to log. This is useful to check if Discord.py is doing something while the log is silent.",
    }

    # # Argument Class Container Metadata
    ARG_PLAIN_CONTAINER_NAME: Final[str] = "ArgsContainer"
    # # Constraints

    __date_on_exec : datetime = datetime.now()
    __eval_date_on_exec : str = __date_on_exec.strftime("%m/%d/%y — %I:%M:%S %p")
    MAXIMUM_RUNTIME_SECONDS = 10

    """
        The following constants is a mapped dictionary structure. It will be used to evaluate environment variable's values
        and serialize as they respect the `expected_type` per fields. A `fallback_value` will be used if a cerrtain function fails
        to serialize a certain value. Keep in mind that fallback is supported for optional inputs only!
    """
    ENV_STRUCT_CONSTRAINTS : Final[dict[str, Any]] = { # ! Check /action.yml for more information.
        # # Required Inputs
        "DISCORD_BOT_TOKEN": {
            "expected_type": str,
            "fallback_value": None,
            "raise_on_failed_type": True
        },
        "DISCORD_USER_ID": {
            "expected_type": int,
            "fallback_value": None,
            "raise_on_failed_type": True
        },
        "PROFILE_REPOSITORY": {
            "expected_type": str,
            "fallback_value": None,
            "raise_on_failed_type": True
        },
        "WORKFLOW_TOKEN": {
            "expected_type": str,
            "fallback_value": None,
            "raise_on_failed_type": True
        },
        # # Optional Inputs — Extensibility and Customization
        "ALLOW_PM_ON_CLICK": {
            "expected_type": bool,
            "fallback_value": False,
            "raise_on_failed_type": False
        },
        "APPEND_DETAIL_PRESENCE": {
            "expected_type": bool,
            "fallback_value": False,
            "raise_on_failed_type": False
        },
        "COMMIT_MESSAGE": {
            "expected_type": str,
            "fallback_value": f"Discord Activity Badge Updated as of {__eval_date_on_exec}.",
            "raise_on_failed_type": False
        },
        "SHOW_HOURS_MINUTES_ELAPSED": {
            "expected_type": bool,
            "fallback_value": False,
            "raise_on_failed_type": False
        },
        "SHOW_OTHER_STATUS": {
            "expected_type": bool,
            "fallback_value": False,
            "raise_on_failed_type": False
        },
        "SHOW_TIME_DURATION": {
            "expected_type": bool,
            "fallback_value": False,
            "raise_on_failed_type": False
        },
        # # Optional Inputs — Badge Customizations
        "NO_ACTIVITY_ONLINE_STATUS": {
            "expected_type": str,
            "fallback_value": "Online",
            "raise_on_failed_type": False
        },
        "NO_ACTIVITY_IDLE_STATUS": {
            "expected_type": str,
            "fallback_value": "Idle",
            "raise_on_failed_type": False
        },
        "NO_ACTIVITY_DND_STATUS": {
            "expected_type": str,
            "fallback_value": "Busy",
            "raise_on_failed_type": False
        },
        "NO_ACTIVITY_OFFLINE_STATUS": {
            "expected_type": str,
            "fallback_value": "Offline",
            "raise_on_failed_type": False
        },
        "STATE_ONLINE_COLOR": { # todo: Pick a color of this one and the other 3.
            "expected_type": str,
            "fallback_value": None,
            "raise_on_failed_type": False
        },
        "STATE_IDLE_COLOR": {
            "expected_type": str,
            "fallback_value": None,
            "raise_on_failed_type": False
        },
        "STATE_DND_COLOR": {
            "expected_type": str,
            "fallback_value": None,
            "raise_on_failed_type": False
        },
        "STATE_OFFLINE_COLOR": {
            "expected_type": str,
            "fallback_value": None,
            "raise_on_failed_type": False
        },
        # # Development Inputs
        "IS_DRY_RUN": {
            "expected_type": bool,
            "fallback_value": False,
            "raise_on_failed_type": False
        },
        "DO_NOT_SEND_ERR_REPORTS": {
            "expected_type": bool,
            "fallback_value": False,
            "raise_on_failed_type": False
        },
    }

    # # Discord Client Container Metadata
    DISCORD_DATA_CONTAINER: Final[str] = "UserStatusContainer"
    DISCORD_DATA_CONTAINER_ATTRS: Final[
        dict[str, Any]
    ] = {  # todo: Fill it up later. +  Ref: https://stackoverflow.com/questions/3603502/prevent-creating-new-attributes-outside-init
        "user": {
            "id": None,
            "name": None,
            "discriminator": None,
            "status": {
                "state": None,
                "on_web": None,
                "on_mobile": None,
            },
            "presence": {},  # Contains user's presence activity. Field is known over runtime since we have two distinct types.
        },  # Contains user's information, this excludes the Discord Rich Presence.
    }

    # # Discord Client Data Container Fields
    DISCORD_DATA_FIELD_CUSTOM : Final[str] = "custom_activity"
    DISCORD_DATA_FIELD_GAME : Final[str] = "game_activity"
    DISCORD_DATA_FIELD_PRESENCE : Final[str] = "rich_presence"
    DISCORD_DATA_FIELD_UNSPECIFIED: Final[str] = "unspecified_activity"


    DISCORD_ON_READY_MSG: Final[
        str
    ] = "Client (%s) is ready for evaluation of user's activity presence."

    # # Discord Client Intents
    DISCORD_CLIENT_INTENTS: Intents = Intents.none()
    DISCORD_CLIENT_INTENTS.guilds = True
    DISCORD_CLIENT_INTENTS.members = True
    DISCORD_CLIENT_INTENTS.presences = True

    # # Identification of Return Codes
    RET_DOTENV_NOT_FOUND: Final[int] = -1

    # # Message of Return Codes

    # # Logger Information
    ROOT_LOCATION: Final[str] = "../"
    ENV_FILENAME: Final[str] = ".env"
    LOGGER_FILENAME: Final[str] = (
        ROOT_LOCATION + strftime("%m%d%Y-%H%M-") + "discord-activity-badge.log"
    )
    LOGGER_OUTPUT_FORMAT: Final[
        str
    ] = "[%(relativeCreated)d ms, %(levelname)s\t]\tat %(module)s.py:%(lineno)d -> %(message)s"

    # # Required Parameters @ ENV
    REQUIRED_PARAMS_IN_ENV: List[str] = [""]  # todo...

    # # Pre-Condition Constraints
    ALLOWABLE_TIME_TO_COMMIT: Final[object] = timeConstraint(
        minutes=30
    )  # todo: Clarify this. This is connected from the workflow recommended refresh rate. Also rate-limits.

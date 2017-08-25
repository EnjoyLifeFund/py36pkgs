# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobPreparationTaskExecutionInformation(Model):
    """Contains information about the execution of a Job Preparation task on a
    compute node.

    :param start_time: The time at which the task started running. Note that
     every time the task is restarted, this value is updated.
    :type start_time: datetime
    :param end_time: The time at which the Job Preparation task completed.
     This property is set only if the task is in the Completed state.
    :type end_time: datetime
    :param state: The current state of the Job Preparation task on the compute
     node. running - the task is currently running (including retrying).
     completed - the task has exited with exit code 0, or the task has
     exhausted its retry limit, or the Batch service was unable to start the
     task due to scheduling errors. Possible values include: 'running',
     'completed'
    :type state: str or :class:`JobPreparationTaskState
     <azure.batch.models.JobPreparationTaskState>`
    :param task_root_directory: The root directory of the Job Preparation task
     on the compute node. You can use this path to retrieve files created by
     the task, such as log files.
    :type task_root_directory: str
    :param task_root_directory_url: The URL to the root directory of the Job
     Preparation task on the compute node.
    :type task_root_directory_url: str
    :param exit_code: The exit code of the program specified on the task
     command line. This parameter is returned only if the task is in the
     completed state. The exit code for a process reflects the specific
     convention implemented by the application developer for that process. If
     you use the exit code value to make decisions in your code, be sure that
     you know the exit code convention used by the application process. Note
     that the exit code may also be generated by the compute node operating
     system, such as when a process is forcibly terminated.
    :type exit_code: int
    :param failure_info: Information describing the task failure, if any. This
     property is set only if the task is in the completed state and encountered
     a failure.
    :type failure_info: :class:`TaskFailureInformation
     <azure.batch.models.TaskFailureInformation>`
    :param retry_count: The number of times the task has been retried by the
     Batch service. Task application failures (non-zero exit code) are retried,
     pre-processing errors (the task could not be run) and file upload errors
     are not retried. The Batch service will retry the task up to the limit
     specified by the constraints.
    :type retry_count: int
    :param last_retry_time: The most recent time at which a retry of the Job
     Preparation task started running. This property is set only if the task
     was retried (i.e. retryCount is nonzero). If present, this is typically
     the same as startTime, but may be different if the task has been restarted
     for reasons other than retry; for example, if the compute node was
     rebooted during a retry, then the startTime is updated but the
     lastRetryTime is not.
    :type last_retry_time: datetime
    :param result: The result of the task execution. If the value is 'failed',
     then the details of the failure can be found in the failureInfo property.
     Possible values include: 'success', 'failure'
    :type result: str or :class:`TaskExecutionResult
     <azure.batch.models.TaskExecutionResult>`
    """

    _validation = {
        'start_time': {'required': True},
        'state': {'required': True},
        'retry_count': {'required': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'JobPreparationTaskState'},
        'task_root_directory': {'key': 'taskRootDirectory', 'type': 'str'},
        'task_root_directory_url': {'key': 'taskRootDirectoryUrl', 'type': 'str'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'failure_info': {'key': 'failureInfo', 'type': 'TaskFailureInformation'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'last_retry_time': {'key': 'lastRetryTime', 'type': 'iso-8601'},
        'result': {'key': 'result', 'type': 'TaskExecutionResult'},
    }

    def __init__(self, start_time, state, retry_count, end_time=None, task_root_directory=None, task_root_directory_url=None, exit_code=None, failure_info=None, last_retry_time=None, result=None):
        self.start_time = start_time
        self.end_time = end_time
        self.state = state
        self.task_root_directory = task_root_directory
        self.task_root_directory_url = task_root_directory_url
        self.exit_code = exit_code
        self.failure_info = failure_info
        self.retry_count = retry_count
        self.last_retry_time = last_retry_time
        self.result = result

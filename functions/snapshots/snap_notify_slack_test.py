# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_event_get_slack_message_attachment_snapshots event_cloudwatch_alarm.json'] = [
    {
        'fallback': 'A new message',
        'mrkdwn_in': [
            'value'
        ],
        'text': 'AWS notification',
        'title': 'bar'
    }
]

snapshots['test_event_get_slack_message_attachment_snapshots event_ec2_autoscaling_launch_failed.json'] = [
    {
        'color': 'danger',
        'fallback': 'EC2 Instance Terminate Unsuccessful',
        'fields': [
            {
                'short': False,
                'title': 'Description',
                'value': '`EC2 Instance Terminate Unsuccessful`'
            },
            {
                'short': True,
                'title': 'Status',
                'value': '`Failed`'
            },
            {
                'short': True,
                'title': 'Message',
                'value': '`message-text`'
            },
            {
                'short': False,
                'title': 'Autoscaling Group',
                'value': '`my-auto-scaling-group`'
            },
            {
                'short': True,
                'title': 'EC2 Instance Id',
                'value': '`i-1234567890abcdef0`'
            },
            {
                'short': False,
                'title': 'Link to Autoscaling group activity',
                'value': 'https://console.aws.amazon.com/ec2autoscaling/home?region=us-east-1#/details/my-auto-scaling-group?view=activity'
            }
        ],
        'text': 'EC2 Instance Terminate Unsuccessful'
    }
]

snapshots['test_event_get_slack_message_attachment_snapshots event_ec2_autoscaling_launch_successful.json'] = [
    {
        'color': 'good',
        'fallback': 'EC2 Instance Launch Successful',
        'fields': [
            {
                'short': False,
                'title': 'Description',
                'value': '`EC2 Instance Launch Successful`'
            },
            {
                'short': True,
                'title': 'Status',
                'value': '`InProgress`'
            },
            {
                'short': True,
                'title': 'Message',
                'value': '``'
            },
            {
                'short': False,
                'title': 'Autoscaling Group',
                'value': '`my-auto-scaling-group`'
            },
            {
                'short': True,
                'title': 'EC2 Instance Id',
                'value': '`i-1234567890abcdef0`'
            },
            {
                'short': False,
                'title': 'Link to Autoscaling group activity',
                'value': 'https://console.aws.amazon.com/ec2autoscaling/home?region=us-east-1#/details/my-auto-scaling-group?view=activity'
            }
        ],
        'text': 'EC2 Instance Launch Successful'
    }
]

snapshots['test_event_get_slack_message_attachment_snapshots event_guardduty_finding_high.json'] = [
    {
        'color': 'danger',
        'fallback': 'GuardDuty Finding: SAMPLE Unprotected port on EC2 instance i-123123123 is being probed',
        'fields': [
            {
                'short': False,
                'title': 'Description',
                'value': '`EC2 instance has an unprotected port which is being probed by a known malicious host.`'
            },
            {
                'short': False,
                'title': 'Finding Type',
                'value': '`Recon:EC2 PortProbeUnprotectedPort`'
            },
            {
                'short': True,
                'title': 'First Seen',
                'value': '`2020-01-02T01:02:03Z`'
            },
            {
                'short': True,
                'title': 'Last Seen',
                'value': '`2020-01-03T01:02:03Z`'
            },
            {
                'short': True,
                'title': 'Severity',
                'value': '`High`'
            },
            {
                'short': True,
                'title': 'Count',
                'value': '`1234`'
            },
            {
                'short': False,
                'title': 'Link to Finding',
                'value': 'https://console.aws.amazon.com/guardduty/home?region=us-east-1#/findings?search=id%3Dsample-id-2'
            }
        ],
        'text': 'AWS GuardDuty Finding - SAMPLE Unprotected port on EC2 instance i-123123123 is being probed'
    }
]

snapshots['test_event_get_slack_message_attachment_snapshots event_guardduty_finding_low.json'] = [
    {
        'color': '#777777',
        'fallback': 'GuardDuty Finding: SAMPLE Unprotected port on EC2 instance i-123123123 is being probed',
        'fields': [
            {
                'short': False,
                'title': 'Description',
                'value': '`EC2 instance has an unprotected port which is being probed by a known malicious host.`'
            },
            {
                'short': False,
                'title': 'Finding Type',
                'value': '`Recon:EC2 PortProbeUnprotectedPort`'
            },
            {
                'short': True,
                'title': 'First Seen',
                'value': '`2020-01-02T01:02:03Z`'
            },
            {
                'short': True,
                'title': 'Last Seen',
                'value': '`2020-01-03T01:02:03Z`'
            },
            {
                'short': True,
                'title': 'Severity',
                'value': '`Low`'
            },
            {
                'short': True,
                'title': 'Count',
                'value': '`1234`'
            },
            {
                'short': False,
                'title': 'Link to Finding',
                'value': 'https://console.aws.amazon.com/guardduty/home?region=us-east-1#/findings?search=id%3Dsample-id-2'
            }
        ],
        'text': 'AWS GuardDuty Finding - SAMPLE Unprotected port on EC2 instance i-123123123 is being probed'
    }
]

snapshots['test_event_get_slack_message_attachment_snapshots event_guardduty_finding_medium.json'] = [
    {
        'color': 'warning',
        'fallback': 'GuardDuty Finding: SAMPLE Unprotected port on EC2 instance i-123123123 is being probed',
        'fields': [
            {
                'short': False,
                'title': 'Description',
                'value': '`EC2 instance has an unprotected port which is being probed by a known malicious host.`'
            },
            {
                'short': False,
                'title': 'Finding Type',
                'value': '`Recon:EC2 PortProbeUnprotectedPort`'
            },
            {
                'short': True,
                'title': 'First Seen',
                'value': '`2020-01-02T01:02:03Z`'
            },
            {
                'short': True,
                'title': 'Last Seen',
                'value': '`2020-01-03T01:02:03Z`'
            },
            {
                'short': True,
                'title': 'Severity',
                'value': '`Medium`'
            },
            {
                'short': True,
                'title': 'Count',
                'value': '`1234`'
            },
            {
                'short': False,
                'title': 'Link to Finding',
                'value': 'https://console.aws.amazon.com/guardduty/home?region=us-east-1#/findings?search=id%3Dsample-id-2'
            }
        ],
        'text': 'AWS GuardDuty Finding - SAMPLE Unprotected port on EC2 instance i-123123123 is being probed'
    }
]

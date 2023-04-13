# pylint: disable=too-many-lines
cached = [
    "aws-sso-assignment.json",
    "aws-ec2-transitgatewayroutetablepropagation.json",
    "aws-ecs-service.json",
    "aws-ram-resourceshare.json",
    "aws-dynamodb-table.json",
    "aws-ec2-securitygroupegress.json",
    "aws-ec2-localgatewayroutetablevpcassociation.json",
    "aws-config-configurationrecorder.json",
    "aws-ec2-networkperformancemetricsubscription.json",
    "aws-cloudfront-continuousdeploymentpolicy.json",
    "aws-ecr-replicationconfiguration.json",
    "aws-rds-dbinstance.json",
    "aws-ec2-vpcdhcpoptionsassociation.json",
    "aws-ec2-networkacl.json",
    "aws-logs-resourcepolicy.json",
    "aws-ec2-networkaclentry.json",
    "aws-transfer-certificate.json",
    "aws-route53resolver-firewalldomainlist.json",
    "aws-appconfig-application.json",
    "aws-lambda-url.json",
    "aws-autoscaling-warmpool.json",
    "aws-applicationautoscaling-scalabletarget.json",
    "aws-config-storedquery.json",
    "aws-acmpca-permission.json",
    "aws-transfer-server.json",
    "aws-ecs-primarytaskset.json",
    "aws-autoscaling-autoscalinggroup.json",
    "aws-wafv2-regexpatternset.json",
    "aws-eks-fargateprofile.json",
    "aws-route53-dnssec.json",
    "aws-ec2-transitgatewayroutetable.json",
    "aws-route53-recordset.json",
    "aws-elasticache-securitygroup.json",
    "aws-cloudtrail-eventdatastore.json",
    "aws-kinesisfirehose-deliverystream.json",
    "aws-sagemaker-coderepository.json",
    "aws-imagebuilder-component.json",
    "aws-ses-configurationseteventdestination.json",
    "aws-appmesh-route.json",
    "aws-organizations-resourcepolicy.json",
    "aws-ec2-transitgatewaymulticastgroupsource.json",
    "aws-transfer-profile.json",
    "aws-appsync-domainname.json",
    "aws-fms-policy.json",
    "aws-cloudfront-realtimelogconfig.json",
    "aws-sagemaker-pipeline.json",
    "aws-cloudtrail-channel.json",
    "aws-lakeformation-datacellsfilter.json",
    "aws-datasync-locationhdfs.json",
    "aws-events-archive.json",
    "aws-msk-cluster.json",
    "aws-codepipeline-pipeline.json",
    "aws-config-configurationaggregator.json",
    "aws-imagebuilder-imagepipeline.json",
    "aws-elasticloadbalancingv2-listenercertificate.json",
    "aws-cloudformation-moduleversion.json",
    "aws-synthetics-canary.json",
    "aws-sns-subscription.json",
    "aws-appmesh-mesh.json",
    "aws-ec2-natgateway.json",
    "aws-transfer-workflow.json",
    "aws-appconfig-deploymentstrategy.json",
    "aws-elasticache-usergroup.json",
    "aws-imagebuilder-imagerecipe.json",
    "aws-opsworks-elasticloadbalancerattachment.json",
    "aws-appmesh-virtualservice.json",
    "aws-s3objectlambda-accesspointpolicy.json",
    "aws-elasticache-replicationgroup.json",
    "aws-cloudformation-moduledefaultversion.json",
    "aws-sso-permissionset.json",
    "aws-servicecatalog-cloudformationprovisionedproduct.json",
    "aws-logs-metricfilter.json",
    "aws-lambda-function.json",
    "aws-sns-topic.json",
    "aws-backup-backupselection.json",
    "aws-sagemaker-app.json",
    "aws-ec2-vpcgatewayattachment.json",
    "aws-ec2-vpnconnectionroute.json",
    "aws-ec2-internetgateway.json",
    "aws-ec2-gatewayroutetableassociation.json",
    "aws-wafv2-ipset.json",
    "aws-ssm-document.json",
    "aws-cloudfront-cloudfrontoriginaccessidentity.json",
    "aws-appmesh-gatewayroute.json",
    "aws-autoscaling-launchconfiguration.json",
    "aws-kinesisanalyticsv2-application.json",
    "aws-lambda-alias.json",
    "aws-ec2-transitgatewaymulticastdomainassociation.json",
    "aws-ec2-transitgatewayroutetableassociation.json",
    "aws-appconfig-environment.json",
    "aws-imagebuilder-image.json",
    "aws-elasticache-securitygroupingress.json",
    "aws-rds-dbproxytargetgroup.json",
    "aws-cloudwatch-dashboard.json",
    "aws-cloudwatch-alarm.json",
    "aws-cloudformation-customresource.json",
    "aws-wafv2-rulegroup.json",
    "aws-ses-configurationset.json",
    "aws-elasticache-parametergroup.json",
    "aws-networkfirewall-loggingconfiguration.json",
    "aws-codedeploy-deploymentgroup.json",
    "aws-cloudformation-stackset.json",
    "aws-ec2-route.json",
    "aws-cloudformation-hookversion.json",
    "aws-rolesanywhere-profile.json",
    "aws-xray-resourcepolicy.json",
    "aws-wafv2-loggingconfiguration.json",
    "aws-backup-backupplan.json",
    "aws-imagebuilder-distributionconfiguration.json",
    "aws-lakeformation-permissions.json",
    "aws-cloudfront-publickey.json",
    "aws-identitystore-group.json",
    "aws-datasync-task.json",
    "aws-ecs-taskdefinition.json",
    "aws-sagemaker-model.json",
    "aws-ses-vdmattributes.json",
    "aws-identitystore-groupmembership.json",
    "aws-appsync-functionconfiguration.json",
    "aws-ec2-spotfleet.json",
    "aws-sagemaker-space.json",
    "aws-fms-notificationchannel.json",
    "aws-msk-batchscramsecret.json",
    "aws-s3-bucket.json",
    "aws-emr-securityconfiguration.json",
    "aws-cloudwatch-insightrule.json",
    "aws-batch-schedulingpolicy.json",
    "aws-athena-workgroup.json",
    "aws-iam-servercertificate.json",
    "aws-events-eventbus.json",
    "aws-ssm-maintenancewindowtarget.json",
    "aws-ses-contactlist.json",
    "aws-rds-dbsecuritygroupingress.json",
    "aws-ec2-transitgatewaymulticastgroupmember.json",
    "aws-ec2-volumeattachment.json",
    "aws-applicationinsights-application.json",
    "aws-ecs-clustercapacityproviderassociations.json",
    "aws-appconfig-configurationprofile.json",
    "aws-route53resolver-firewallrulegroup.json",
    "aws-msk-configuration.json",
    "aws-ssm-maintenancewindowtask.json",
    "aws-ec2-transitgatewaymulticastdomain.json",
    "aws-eks-cluster.json",
    "aws-efs-filesystem.json",
    "aws-logs-querydefinition.json",
    "aws-iam-instanceprofile.json",
    "aws-datasync-locationnfs.json",
    "aws-sagemaker-domain.json",
    "aws-certificatemanager-certificate.json",
    "aws-sdb-domain.json",
    "aws-ec2-subnetroutetableassociation.json",
    "aws-servicecatalog-serviceactionassociation.json",
    "aws-imagebuilder-containerrecipe.json",
    "aws-efs-accesspoint.json",
    "aws-redshift-clustersecuritygroupingress.json",
    "aws-servicecatalogappregistry-attributegroupassociation.json",
    "aws-elasticloadbalancingv2-loadbalancer.json",
    "aws-opensearchservice-domain.json",
    "aws-elasticsearch-domain.json",
    "aws-secretsmanager-resourcepolicy.json",
    "aws-cloudformation-hookdefaultversion.json",
    "aws-config-configrule.json",
    "aws-ecs-taskset.json",
    "aws-appsync-apikey.json",
    "aws-acmpca-certificateauthorityactivation.json",
    "aws-ec2-vpc.json",
    "aws-route53-recordsetgroup.json",
    "aws-ec2-localgatewayroute.json",
    "aws-opsworks-app.json",
    "aws-iam-samlprovider.json",
    "aws-cloudfront-keygroup.json",
    "aws-ec2-transitgatewayattachment.json",
    "aws-codedeploy-deploymentconfig.json",
    "aws-servicecatalogappregistry-application.json",
    "aws-backup-backupvault.json",
    "aws-ec2-customergateway.json",
    "aws-scheduler-schedule.json",
    "aws-waf-bytematchset.json",
    "aws-systemsmanagersap-application.json",
    "aws-ec2-routetable.json",
    "aws-rds-dbproxyendpoint.json",
    "aws-datasync-locationsmb.json",
    "aws-rolesanywhere-crl.json",
    "aws-organizations-policy.json",
    "aws-ec2-vpcpeeringconnection.json",
    "aws-networkfirewall-rulegroup.json",
    "aws-kms-key.json",
    "aws-route53resolver-firewallrulegroupassociation.json",
    "aws-route53resolver-resolverqueryloggingconfig.json",
    "aws-ec2-subnet.json",
    "aws-cloudtrail-resourcepolicy.json",
    "aws-s3objectlambda-accesspoint.json",
    "aws-elasticbeanstalk-configurationtemplate.json",
    "aws-sqs-queuepolicy.json",
    "aws-appsync-domainnameapiassociation.json",
    "aws-wafv2-webacl.json",
    "aws-ec2-transitgatewayconnect.json",
    "aws-ec2-securitygroup.json",
    "aws-opsworks-volume.json",
    "aws-ses-emailidentity.json",
    "aws-iam-usertogroupaddition.json",
    "aws-ec2-vpngatewayroutepropagation.json",
    "aws-cloudfront-function.json",
    "aws-ssm-patchbaseline.json",
    "aws-cloudfront-monitoringsubscription.json",
    "aws-efs-mounttarget.json",
    "aws-ec2-vpnconnection.json",
    "aws-iam-user.json",
    "aws-emr-instancegroupconfig.json",
    "aws-ec2-localgatewayroutetablevirtualinterfacegroupassociation.json",
    "aws-s3-bucketpolicy.json",
    "aws-appsync-graphqlschema.json",
    "aws-emr-instancefleetconfig.json",
    "aws-emr-cluster.json",
    "aws-rds-dbcluster.json",
    "aws-transfer-agreement.json",
    "aws-chatbot-slackchannelconfiguration.json",
    "aws-cloudfront-distribution.json",
    "aws-elasticache-subnetgroup.json",
    "aws-xray-group.json",
    "aws-oam-link.json",
    "aws-sagemaker-endpoint.json",
    "aws-networkfirewall-firewall.json",
    "aws-ses-template.json",
    "aws-kms-replicakey.json",
    "aws-redshift-clustersecuritygroup.json",
    "aws-route53-cidrcollection.json",
    "aws-ecr-pullthroughcacherule.json",
    "aws-appconfig-hostedconfigurationversion.json",
    "aws-datasync-locationefs.json",
    "aws-ec2-localgatewayroutetable.json",
    "aws-sagemaker-appimageconfig.json",
    "aws-elasticloadbalancingv2-targetgroup.json",
    "aws-pipes-pipe.json",
    "aws-cloudformation-macro.json",
    "aws-sagemaker-workteam.json",
    "aws-secretsmanager-secret.json",
    "aws-elasticache-user.json",
    "aws-codedeploy-application.json",
    "aws-lakeformation-principalpermissions.json",
    "aws-datasync-locations3.json",
    "aws-autoscaling-lifecyclehook.json",
    "aws-ec2-networkinterface.json",
    "aws-appsync-resolver.json",
    "aws-rolesanywhere-trustanchor.json",
    "aws-route53resolver-resolverqueryloggingconfigassociation.json",
    "aws-rds-optiongroup.json",
    "aws-opsworks-userprofile.json",
    "aws-ssm-maintenancewindow.json",
    "aws-lakeformation-tagassociation.json",
    "aws-imagebuilder-infrastructureconfiguration.json",
    "aws-sagemaker-notebookinstance.json",
    "aws-sso-instanceaccesscontrolattributeconfiguration.json",
    "aws-cloudwatch-anomalydetector.json",
    "aws-servicecatalog-serviceaction.json",
    "aws-cloudfront-originaccesscontrol.json",
    "aws-secretsmanager-rotationschedule.json",
    "aws-lambda-permission.json",
    "aws-networkfirewall-firewallpolicy.json",
    "aws-eks-identityproviderconfig.json",
    "aws-servicecatalogappregistry-attributegroup.json",
    "aws-appsync-graphqlapi.json",
    "aws-ec2-egressonlyinternetgateway.json",
    "aws-ec2-vpccidrblock.json",
    "aws-acmpca-certificateauthority.json",
    "aws-athena-preparedstatement.json",
    "aws-autoscaling-scheduledaction.json",
    "aws-lakeformation-resource.json",
    "aws-ec2-vpcendpoint.json",
    "aws-rds-eventsubscription.json",
    "aws-config-aggregationauthorization.json",
    "aws-datasync-agent.json",
    "aws-logs-loggroup.json",
    "aws-ec2-placementgroup.json",
    "aws-organizations-account.json",
    "aws-ecr-repository.json",
    "aws-ses-dedicatedippool.json",
    "aws-ec2-keypair.json",
    "aws-fsx-filesystem.json",
    "aws-ec2-eipassociation.json",
    "aws-elasticbeanstalk-application.json",
    "aws-ec2-capacityreservation.json",
    "aws-elasticloadbalancing-loadbalancer.json",
    "aws-transfer-user.json",
    "aws-rds-dbclusterparametergroup.json",
    "aws-appmesh-virtualrouter.json",
    "aws-scheduler-schedulegroup.json",
    "aws-route53-keysigningkey.json",
    "aws-config-remediationconfiguration.json",
    "aws-athena-datacatalog.json",
    "aws-sagemaker-userprofile.json",
    "aws-ec2-prefixlist.json",
    "aws-ec2-instance.json",
    "aws-appmesh-virtualgateway.json",
    "aws-waf-sqlinjectionmatchset.json",
    "aws-ec2-transitgatewayvpcattachment.json",
    "aws-amazonmq-broker.json",
    "aws-ssm-association.json",
    "aws-cloudfront-responseheaderspolicy.json",
    "aws-transfer-connector.json",
    "aws-appmesh-virtualnode.json",
    "aws-wafv2-webaclassociation.json",
    "aws-oam-sink.json",
    "aws-acmpca-certificate.json",
    "aws-workspaces-workspace.json",
    "aws-datasync-locationobjectstorage.json",
    "aws-ecs-capacityprovider.json",
    "aws-elasticache-cachecluster.json",
    "aws-sagemaker-modelcard.json",
    "aws-logs-destination.json",
    "aws-eks-nodegroup.json",
    "aws-organizations-organizationalunit.json",
    "aws-appsync-datasource.json",
    "aws-sqs-queue.json",
    "aws-ec2-securitygroupingress.json",
    "aws-batch-computeenvironment.json",
    "aws-events-eventbuspolicy.json",
    "aws-lakeformation-datalakesettings.json",
    "aws-autoscaling-scalingpolicy.json",
    "aws-ecr-registrypolicy.json",
    "aws-rds-dbsecuritygroup.json",
    "aws-cloudwatch-metricstream.json",
    "aws-config-deliverychannel.json",
    "aws-iam-oidcprovider.json",
    "aws-lakeformation-tag.json",
    "aws-servicecatalogappregistry-resourceassociation.json",
    "aws-ec2-vpngateway.json",
    "aws-cloudformation-stack.json",
    "aws-resourcegroups-group.json",
    "aws-ec2-transitgatewaypeeringattachment.json",
    "aws-cloudfront-cachepolicy.json",
    "aws-rds-dbsubnetgroup.json",
    "aws-amazonmq-configuration.json",
    "aws-appconfig-deployment.json",
    "aws-accessanalyzer-analyzer.json",
    "aws-ec2-ec2fleet.json",
    "aws-ec2-vpcendpointservice.json",
    "aws-iam-managedpolicy.json",
    "aws-cloudfront-originrequestpolicy.json",
    "aws-elasticbeanstalk-environment.json",
    "aws-lambda-version.json",
    "aws-ec2-dhcpoptions.json",
    "aws-cloudformation-hooktypeconfig.json",
    "aws-ec2-volume.json",
    "aws-ec2-eip.json",
    "aws-chatbot-microsoftteamschannelconfiguration.json",
    "aws-rds-dbproxy.json",
    "aws-rds-dbparametergroup.json",
    "aws-s3-accesspoint.json",
    "aws-batch-jobqueue.json",
    "aws-cloudformation-waitconditionhandle.json",
    "aws-eks-addon.json",
]
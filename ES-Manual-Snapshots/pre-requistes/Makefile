PROFILE = appointments
ENVIRONMENT = sbx
BRANCH = develop
PREFIX = dev
BasePath = \

.PHONY: explain
explain:
		#                                                                                                                                                        
		# PPPPPPPPPPPPPPPPP   IIIIIIIIIIPPPPPPPPPPPPPPPPP   EEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLL             IIIIIIIIIINNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEE
		# P::::::::::::::::P  I::::::::IP::::::::::::::::P  E::::::::::::::::::::EL:::::::::L             I::::::::IN:::::::N       N::::::NE::::::::::::::::::::E
		# P::::::PPPPPP:::::P I::::::::IP::::::PPPPPP:::::P E::::::::::::::::::::EL:::::::::L             I::::::::IN::::::::N      N::::::NE::::::::::::::::::::E
		# PP:::::P     P:::::PII::::::IIPP:::::P     P:::::PEE::::::EEEEEEEEE::::ELL:::::::LL             II::::::IIN:::::::::N     N::::::NEE::::::EEEEEEEEE::::E
		#  P::::P     P:::::P  I::::I    P::::P     P:::::P  E:::::E       EEEEEE  L:::::L                 I::::I  N::::::::::N    N::::::N  E:::::E       EEEEEE
		#  P::::P     P:::::P  I::::I    P::::P     P:::::P  E:::::E               L:::::L                 I::::I  N:::::::::::N   N::::::N  E:::::E             
		#  P::::PPPPPP:::::P   I::::I    P::::PPPPPP:::::P   E::::::EEEEEEEEEE     L:::::L                 I::::I  N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE   
		#  P:::::::::::::PP    I::::I    P:::::::::::::PP    E:::::::::::::::E     L:::::L                 I::::I  N::::::N N::::N N::::::N  E:::::::::::::::E   
		#  P::::PPPPPPPPP      I::::I    P::::PPPPPPPPP      E:::::::::::::::E     L:::::L                 I::::I  N::::::N  N::::N:::::::N  E:::::::::::::::E   
		#  P::::P              I::::I    P::::P              E::::::EEEEEEEEEE     L:::::L                 I::::I  N::::::N   N:::::::::::N  E::::::EEEEEEEEEE   
		#  P::::P              I::::I    P::::P              E:::::E               L:::::L                 I::::I  N::::::N    N::::::::::N  E:::::E             
		#  P::::P              I::::I    P::::P              E:::::E       EEEEEE  L:::::L         LLLLLL  I::::I  N::::::N     N:::::::::N  E:::::E       EEEEEE
		# PP::::::PP          II::::::IIPP::::::PP          EE::::::EEEEEEEE:::::ELL:::::::LLLLLLLLL:::::LII::::::IIN::::::N      N::::::::NEE::::::EEEEEEEE:::::E
		# P::::::::P          I::::::::IP::::::::P          E::::::::::::::::::::EL::::::::::::::::::::::LI::::::::IN::::::N       N:::::::NE::::::::::::::::::::E
		# P::::::::P          I::::::::IP::::::::P          E::::::::::::::::::::EL::::::::::::::::::::::LI::::::::IN::::::N        N::::::NE::::::::::::::::::::E
		# PPPPPPPPPP          IIIIIIIIIIPPPPPPPPPP          EEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLLIIIIIIIIIINNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEE
		#
		### Targets
		#
		@cat Makefile* | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'



.PHONY: create_bucket
create_bucket: ## Creates a new bucket cloudformation stack in AWS
		make create_update_bucket ACTION=create

.PHONY: update_bucket
update_bucket: ## Updates an existing bucket cloudformation stack in AWS
		make create_update_bucket ACTION=update

.PHONY: create_update_bucket
create_update_bucket: ## Creates or updates the bucket cloudformation stack based on the action
	aws cloudformation $(ACTION)-stack \
	--stack-name ${PREFIX}-$(ENVIRONMENT)-buckets \
	--template-body file://./artifact-store-stack.yaml \
	--profile $(PROFILE) \
	--capabilities CAPABILITY_NAMED_IAM \
	--parameters \
		ParameterKey=StackPrefix,ParameterValue=$(PREFIX) \
		ParameterKey=Environment,ParameterValue=$(ENVIRONMENT) \

.PHONY: create_iam_role
create_iam_role: ## Creates or updates the bucket cloudformation stack based on the action
	aws iam create-role --role-name es-snapshots-lambda \
      --profile $(PROFILE) \
      --assume-role-policy-document file://../json_file/trust_policy.json



.PHONY: put_iam_role_policy
put_iam_role_policy: ## Creates or updates the bucket cloudformation stack based on the action
	aws iam put-role-policy --role-name es-snapshots-lambda \
    --profile $(PROFILE) \
    --policy-name es_snapshots \
    --policy-document file://../json_file/es_snapshotbucket.json




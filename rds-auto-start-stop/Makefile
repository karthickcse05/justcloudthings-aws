PROFILE = appointments
ENVIRONMENT = sbx
BRANCH = develop
PREFIX = for-test
ClusterNameValue = test


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

.PHONY: package
package: ## Stores the PAT code for GITHUB in secure storage
	aws cloudformation package \
    --template-file "rds-auto-start-stop.yaml" \
    --s3-bucket  ${PREFIX}-$(ENVIRONMENT)-artifacts \
    --output-template-file "outputs\rds-auto-start-stop-release.yaml" \
	--profile  $(PROFILE) \


.PHONY: create_rds
create_rds: ## Creates a rds start stop  cloudformation stack in AWS
		make deploy ACTION=create

.PHONY: update_rds
update_rds: ## Updates an existing rds start stop cloudformation stack in AWS
		make deploy ACTION=update


.PHONY: deploy
deploy:  ## deploy the rds start stop cloudformation stack in AWS
	aws cloudformation $(ACTION)-stack \
	--stack-name ${PREFIX}-$(ENVIRONMENT)-rdsstartstop \
	--template-body file://./outputs/rds-auto-start-stop-release.yaml \
	--profile $(PROFILE) \
	--capabilities  CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
	--parameters \
		ParameterKey=ClusterName,ParameterValue=$(ClusterNameValue) \



PROFILE = appointments
ENVIRONMENT = sbx
BRANCH = develop
PREFIX = dev
ESENDPOINT="endpointname" # bucket must exist in the SAME region the deployment is taking place
BUCKETNAME="bucketname"
AWSACCOUNTID="xxxxxx"
AWSPROFILE="xxxx"



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





.PHONY: create_lambda
create_lambda: ## Creates erpo lambda
	aws lambda create-function \
      --profile ${AWS_PROFILE} \
      --function-name es-register-repo-lambda \
      --environment "Variables={es_endpoint=$(ESENDPOINT),es_bucket=$(BUCKETNAME),es_accountid=$(AWSACCOUNTID)}" \
      --zip-file fileb://build/register-repo.zip \
      --description "Registering Repo" \
      --role arn:aws:iam::$(AWSACCOUNTID):role/es-snapshots-lambda \
      --handler es-snapshots.lambda_handler \
      --runtime python2.7 \
      --timeout 300





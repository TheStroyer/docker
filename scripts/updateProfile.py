#####################################################################################
#                                                                                   #
#  Script to                                                        #
#                                                                                   #
#  Usage :                 # 
#                                                                                   #
#####################################################################################

def setProfile():

	AdminTask.importWasprofile('[-archive /home/was/was9-lex-profile.car]')
	AdminConfig.save()

setProfile()	
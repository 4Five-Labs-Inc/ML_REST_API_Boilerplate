# Define all service methods here
class Services:

    def __init__(self):
        self.message = 'It works ;)'

    """
        sample check_get method to check GET api
        :return: string
    """
    def check_get(self):
        return (self.message)
    
    """
        sample check_post method to check POST api
        :param name: string
        :return: string
    """
    def check_post(self, name):
        return ("Hello %s, %s" % (name, self.message))
from eucadeploy.plugins.validator.validatorplugin import ValidatorPlugin

class Storage(ValidatorPlugin):
    def validate(self):
        self.topology = self.environment['default_attributes']['eucalyptus']['topology']
        if 'system-properties' in self.environment['default_attributes']['eucalyptus']:
            self.systemproperties = self.environment['default_attributes']['eucalyptus']['system-properties']
        for name in self.topology['clusters'].keys():
            if 'storage-backend' in self.topology['clusters'][name]:
                if 'netapp' in self.topology['clusters'][name]['storage-backend']:
                    netapp_props = [name + '.storage.chapuser', name + '.storage.ncpaths', name + '.storage.scpaths',
                                    name + '.storage.sanhost', name + '.storage.sanpassword', name + '.storage.sanuser',
                                    name + '.storage.vservername']
                    for val in netapp_props:
                        assert self.systemproperties[val]
                        self.success('Netapp system property ' + val + ' is valid.')


#                    raise AssertionError("Netapp system property " + name + '.storage.chapuser is invalid')

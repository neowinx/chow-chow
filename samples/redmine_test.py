from redmine import Redmine

redmine = Redmine('http://demo.redmine.org', username='foo', password='bar')
project = redmine.project.get('tor')

print 'project.id', project.id
print 'project.identifier', project.identifier
print 'project.created_on', project.created_on
print 'len(project.issues)', len(project.issues)
if len(project.issues) > 0:
    print 'project.issues[0]', dir(project.issues[0])
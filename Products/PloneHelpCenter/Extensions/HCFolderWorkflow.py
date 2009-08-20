#
# Generated by dumpDCWorkflow.py written by Sebastien Bigaret
# Original workflow id/title: folder_workflow/Folder Workflow [Plone]
# Date: 2004/08/11 08:48:26.016 GMT-4
#
# WARNING: this dumps does NOT contain any scripts you might have added to
# the workflow, IT IS YOUR RESPONSABILITY TO MAKE BACKUPS FOR THESE SCRIPTS.
#
# No script detected in this workflow
# 
"""
Programmatically creates a workflow type
"""
__version__ = "$Revision: 1.2 $"[11:-2]

from Products.CMFCore.WorkflowTool import addWorkflowFactory
from Products.DCWorkflow.DCWorkflow import DCWorkflowDefinition
from Products.PloneHelpCenter.config import *

def setupFolder_workflow(wf):
    "..."
    wf.setProperties(title='Folder Workflow [Plone]')

    for s in ['visible', 'private', 'published']:
        wf.states.addState(s)
    for t in ['retract', 'hide', 'publish', 'show']:
        wf.transitions.addTransition(t)
    for v in ['action', 'review_history', 'actor', 'comments', 'time']:
        wf.variables.addVariable(v)
    for l in ['reviewer_queue']:
        wf.worklists.addWorklist(l)
    for p in ('Add portal content','Access contents information', 
                'Modify portal content', 'View', 'List folder contents',
                ADD_DOCUMENTATION_PERMISSION):
        wf.addManagedPermission(p)
        

    ## Initial State
    wf.states.setInitialState('published')

    ## States initialization
    sdef = wf.states['visible']
    sdef.setProperties(title="""Visible""",
                       transitions=('hide', 'publish'))
    sdef.setPermission('Access contents information', 1, ['Anonymous', 'Manager', 'Reviewer'])
    sdef.setPermission('Modify portal content', 0, ['Manager', 'Owner'])
    sdef.setPermission('View', 1, ['Anonymous', 'Manager', 'Reviewer'])
    sdef.setPermission('List folder contents', 0, ['Manager', 'Owner', 'Member'])
    sdef.setPermission('Add portal content', 0, ['Manager', 'Owner',])
    sdef.setPermission(ADD_DOCUMENTATION_PERMISSION, 0, ['Manager', 'Owner',])
    

    sdef = wf.states['private']
    sdef.setProperties(title="""Private""",
                       transitions=('publish', 'show'))
    sdef.setPermission('Access contents information', 0, ['Manager', 'Owner'])
    sdef.setPermission('Modify portal content', 0, ['Manager', 'Owner'])
    sdef.setPermission('View', 0, ['Manager', 'Owner'])
    sdef.setPermission('List folder contents', 0, ['Manager', 'Owner'])
    sdef.setPermission('Add portal content', 0, ['Manager', 'Owner',])
    sdef.setPermission(ADD_DOCUMENTATION_PERMISSION, 0, ['Manager', 'Owner',])

    sdef = wf.states['published']
    sdef.setProperties(title="""Open for submissions""",
                       transitions=('hide', 'retract'))
    sdef.setPermission('Access contents information', 1, ['Anonymous', 'Manager'])
    sdef.setPermission('Modify portal content', 0, ['Manager', 'Owner'])
    sdef.setPermission('View', 1, ['Anonymous', 'Manager'])
    sdef.setPermission('List folder contents', 1, ['Anonymous'])
    sdef.setPermission('Add portal content', 0, ['Manager', 'Owner','Member'])
    sdef.setPermission(ADD_DOCUMENTATION_PERMISSION, 0, ['Manager', 'Owner','Member'])

    ## Transitions initialization
    tdef = wf.transitions['retract']
    tdef.setProperties(title="""Close for submissions""",
                       new_state_id="""visible""",
                       trigger_type=1,
                       script_name="""""",
                       after_script_name="""""",
                       actbox_name="""Close for submissions""",
                       actbox_url="""%(content_url)s/content_retract_form""",
                       actbox_category="""workflow""",
                       props={'guard_permissions': 'Request review'},
                       )

    tdef = wf.transitions['hide']
    tdef.setProperties(title="""Hide""",
                       new_state_id="""private""",
                       trigger_type=1,
                       script_name="""""",
                       after_script_name="""""",
                       actbox_name="""Hide""",
                       actbox_url="""%(content_url)s/content_hide_form""",
                       actbox_category="""workflow""",
                       props={'guard_roles': 'Owner'},
                       )

    tdef = wf.transitions['publish']
    tdef.setProperties(title="""Open for submissions""",
                       new_state_id="""published""",
                       trigger_type=1,
                       script_name="""""",
                       after_script_name="""""",
                       actbox_name="""Open for submissions""",
                       actbox_url="""%(content_url)s/content_publish_form""",
                       actbox_category="""workflow""",
                       props={'guard_permissions': 'Modify portal content', 'guard_roles': 'Owner; Manager'},
                       )

    tdef = wf.transitions['show']
    tdef.setProperties(title="""Member makes content visible""",
                       new_state_id="""visible""",
                       trigger_type=1,
                       script_name="""""",
                       after_script_name="""""",
                       actbox_name="""Make visible""",
                       actbox_url="""%(content_url)s/content_show_form""",
                       actbox_category="""workflow""",
                       props={'guard_roles': 'Owner'},
                       )

    ## State Variable
    wf.variables.setStateVar('review_state')

    ## Variables initialization
    vdef = wf.variables['action']
    vdef.setProperties(description="""The last transition""",
                       default_value="""""",
                       default_expr="""transition/getId|nothing""",
                       for_catalog=0,
                       for_status=1,
                       update_always=1,
                       props=None)

    vdef = wf.variables['review_history']
    vdef.setProperties(description="""Provides access to workflow history""",
                       default_value="""""",
                       default_expr="""state_change/getHistory""",
                       for_catalog=0,
                       for_status=0,
                       update_always=0,
                       props={'guard_permissions': 'Request review; Review portal content'})

    vdef = wf.variables['actor']
    vdef.setProperties(description="""The ID of the user who performed the last transition""",
                       default_value="""""",
                       default_expr="""user/getId""",
                       for_catalog=0,
                       for_status=1,
                       update_always=1,
                       props=None)

    vdef = wf.variables['comments']
    vdef.setProperties(description="""Comments about the last transition""",
                       default_value="""""",
                       default_expr="""python:state_change.kwargs.get('comment', '')""",
                       for_catalog=0,
                       for_status=1,
                       update_always=1,
                       props=None)

    vdef = wf.variables['time']
    vdef.setProperties(description="""Time of the last transition""",
                       default_value="""""",
                       default_expr="""state_change/getDateTime""",
                       for_catalog=0,
                       for_status=1,
                       update_always=1,
                       props=None)

    ## Worklists Initialization
    ldef = wf.worklists['reviewer_queue']
    ldef.setProperties(description="""Reviewer tasks""",
                       actbox_name="""Pending (%(count)d)""",
                       actbox_url="""%(portal_url)s/search?review_state=pending""",
                       actbox_category="""global""",
                       props={'guard_permissions': 'Review portal content', 'var_match_review_state': 'pending'})


def createFolder_workflow(id):
    "..."
    ob = DCWorkflowDefinition(id)
    setupFolder_workflow(ob)
    return ob

def install():
    addWorkflowFactory(createFolder_workflow,
        id='helpcenterfolder_workflow',
                   title='Workflow for Help Center Folders.')

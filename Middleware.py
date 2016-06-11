import time  
  
from nova import log as logging  
from nova import wsgi as base_wsgi  
from nova.api.openstack import wsgi  
  
  
LOG = logging.getLogger('nova.api.audit')  
  
class AuditMiddleware(base_wsgi.Middleware):  
    """store POST/PUT/DELETE api request for audit."""  
    def __init__(self, application, audit_methods='POST,PUT,DELETE'):  
        base_wsgi.Middleware.__init__(self, application)  
        self._audit_methods = audit_methods.split(",")  
  
    def process_request(self, req):  
        self._need_audit = req.method in self._audit_methods  
        if self._need_audit:  
            self._request = req  
            self._requested_at = time.time()  
  
    def process_response(self, response):  
        if self._need_audit and response.status_int >= 200 and response.status_int < 300:  
            self._store_log(response)  
        return response  
  
    def _store_log(self, response):  
        req = self._request  
        LOG.info("tenant: %s, user: %s, %s: %s, at: %s",  
            req.headers.get('X-Tenant', 'admin'),  
            req.headers.get('X-User', 'admin'),  
            req.method,  
            req.path_info,  
            self._requested_at)  

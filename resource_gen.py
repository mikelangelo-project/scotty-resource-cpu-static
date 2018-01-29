import logging

logger = logging.getLogger(__name__)


def deploy(context):
  resource = context.v1.resource
  endpoint = resource.params['endpoint']
  logger.debug('Static Resource endpoint {}'.format(endpoint))
  return endpoint

def clean(context):
  pass

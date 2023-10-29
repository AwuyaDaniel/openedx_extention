import logging

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserGreetingsSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
log = logging.getLogger(__name__)
def check_request_arguments(req, fields: list):
    # Check if all fields are added to the request
    try:
        unavailable_fields = [field for field in fields if not req.data.get(field)]
        if not unavailable_fields:
            return {"status": True, "unavailable_fields": unavailable_fields}
        else:
            return {"status": False, "unavailable_fields": unavailable_fields}
    except Exception as E:
        return {"status": False, "unavailable_fields": E}

def get_user(token, authentication):
    # Get User Information through Token
    token_obj = token.objects.get(key=authentication[1])
    user_info = token_obj.user
    return user_info


class UserGreetings(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserGreetingsSerializer

    def post(self, request, *args, **kwargs):
        args = check_request_arguments(request, ['greeting'])
        authentication = request.headers.get('Authorization', '').split()

        if not args['status']:
            return Response({'error': f'The following field(s) are required', 'field(s)': args["unavailable_fields"]},
                            status.HTTP_400_BAD_REQUEST)
        else:
            user = get_user(Token, authentication)
            request.data['user'] = user.id
            return self.create(request, *args, **kwargs)

# log.info(
#             "student_dashboard() - initiating after user authentication for {username}".format(
#                 username=request.user.username
#             )
#         )
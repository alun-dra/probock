
import traceback
from django.db import DatabaseError
from django.db.transaction import atomic

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


from users.models.user import User

from users.serializer.userSerializer import UserSerializer

class UsersViewset(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @atomic
    @action(detail=False, methods=['GET'], url_path='UserList')
    def GetUsers(self, request, *args, **kwargs):
        """
        @url: http://{{host}}:{{port}}/api/users/userEnpoit/UserList
        @successful_response: HTTP 200 (OK)
        @description: Obtiene una lista de todos los usuarios.
        """


        resp = {}
        data = {}
        status_err = status.HTTP_200_OK
        try:
            users = self.get_queryset()
            serializer = self.get_serializer(users, many=True)
            data = {'users': serializer.data}

            if not data['users']:
                return Response({'detail': 'No se encontraron usuarios'}, status=status.HTTP_200_OK)

            return Response({'data': data}, status=status.HTTP_200_OK)
            
        except DatabaseError:
            return Response({"detail": "Error en la base de datos."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            # Si hay otro tipo de error, devuelve una respuesta 500 con un mensaje de error genérico
            print(str(e))
            traceback.print_exc()
            return Response({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'errors': 'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        finally:
            resp['code'] = status_err
            resp['data'] = data
            return Response(resp)

        
    
    @atomic
    @action(detail=True, methods=['GET'], url_path='UserList')
    def GetUserById(self, request, pk=None, *args, **kwargs):
        """
            @url: http://{{host}}:{{port}}/api/users/userEnpoit/{{id}}/UserList
            @succesful_response: HTTP 200 (OK)
            @description: obtiene la informacion de un solo usuario
        """
        resp = {}
        data = {}
        status_err = status.HTTP_200_OK

        try:
            user = self.get_queryset().get(id=pk)
            serializer = self.get_serializer(user)
            data = serializer.data
        except User.DoesNotExist:
            return Response({"detail": "No se encontró el usuario especificado."}, status=404)

        except DatabaseError:
            return Response({"detail": "Error en la base de datos."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            # Si hay otro tipo de error, devuelve una respuesta 500 con un mensaje de error genérico
            print(str(e))
            traceback.print_exc()
            return Response({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'errors': 'internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        finally:
            resp['code'] = status_err
            resp['data'] = data
            return Response(resp)
    
    @atomic
    @action(detail=True, methods=['PUT'], url_path='UserUpdate')
    def UpdateUser(self, request, id=None, *args, **kwargs):
        """
            @url: http://{{host}}:{{port}}/api/users/userEnpoit/{{id}}/UserUpdate/
            @succesful_response: HTTP 200 (OK)
            @description: actualiza la informacion de un usuario
        """

        try:
            user = self.get_queryset().get(id=id)
        except User.DoesNotExist:
            return Response({"detail": "No se encontró el usuario especificado."}, status=404)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'email' in serializer.validated_data:
            existing_user = User.objects.filter(email=serializer.validated_data['email']).exclude(id=user.id).first()
            if existing_user:
                return Response({"detail": "Ya existe un usuario con este correo electrónico."}, status=400)

        serializer.save()

        return Response(serializer.data)
    
    @atomic
    @action(detail=True, methods=['DELETE'], url_path='UserDelete')
    def DeleteUser(self, request, id=None, *args, **kwargs):
        """
            @url: http://{{host}}:{{port}}/api/users/userEnpoit/{{id}}/UserDelete
            @succesful_response: HTTP 200 (OK)
            @description: elimina un usuario mediante el ID
        """

        try:
            user = self.get_queryset().get(id=id)
        except User.DoesNotExist:
            return Response({"detail": "No se encontró el usuario especificado."}, status=404)

        user.delete()

        return Response({"detail": "Usuario eliminado correctamente."})
    

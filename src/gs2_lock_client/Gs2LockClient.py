# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2LockClient(AbstractGs2Client):

    ENDPOINT = "lock"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2LockClient, self).__init__(credential, region)

    def create_lock_pool(self, request):
        """
        ロックプールを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_lock_client.control.CreateLockPoolRequest.CreateLockPoolRequest
        :return: 結果
        :rtype: gs2_lock_client.control.CreateLockPoolResult.CreateLockPoolResult
        """
        body = { 
            "name": request.get_name(),
            "serviceClass": request.get_service_class(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.CreateLockPoolRequest import CreateLockPoolRequest
        from gs2_lock_client.control.CreateLockPoolResult import CreateLockPoolResult
        return CreateLockPoolResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool",
            service=self.ENDPOINT,
            component=CreateLockPoolRequest.Constant.MODULE,
            target_function=CreateLockPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_lock_pool(self, request):
        """
        ロックプールを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_lock_client.control.DeleteLockPoolRequest.DeleteLockPoolRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.DeleteLockPoolRequest import DeleteLockPoolRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "",
            service=self.ENDPOINT,
            component=DeleteLockPoolRequest.Constant.MODULE,
            target_function=DeleteLockPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_lock_pool(self, request):
        """
        ロックプールの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_lock_client.control.DescribeLockPoolRequest.DescribeLockPoolRequest
        :return: 結果
        :rtype: gs2_lock_client.control.DescribeLockPoolResult.DescribeLockPoolResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.DescribeLockPoolRequest import DescribeLockPoolRequest

        from gs2_lock_client.control.DescribeLockPoolResult import DescribeLockPoolResult
        return DescribeLockPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool",
            service=self.ENDPOINT,
            component=DescribeLockPoolRequest.Constant.MODULE,
            target_function=DescribeLockPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_service_class(self, request):
        """
        サービスクラスの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_lock_client.control.DescribeServiceClassRequest.DescribeServiceClassRequest
        :return: 結果
        :rtype: gs2_lock_client.control.DescribeServiceClassResult.DescribeServiceClassResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.DescribeServiceClassRequest import DescribeServiceClassRequest

        from gs2_lock_client.control.DescribeServiceClassResult import DescribeServiceClassResult
        return DescribeServiceClassResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/serviceClass",
            service=self.ENDPOINT,
            component=DescribeServiceClassRequest.Constant.MODULE,
            target_function=DescribeServiceClassRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_lock_pool(self, request):
        """
        ロックプールを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_lock_client.control.GetLockPoolRequest.GetLockPoolRequest
        :return: 結果
        :rtype: gs2_lock_client.control.GetLockPoolResult.GetLockPoolResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.GetLockPoolRequest import GetLockPoolRequest

        from gs2_lock_client.control.GetLockPoolResult import GetLockPoolResult
        return GetLockPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "",
            service=self.ENDPOINT,
            component=GetLockPoolRequest.Constant.MODULE,
            target_function=GetLockPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_lock_pool_status(self, request):
        """
        ロックプールの状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_lock_client.control.GetLockPoolStatusRequest.GetLockPoolStatusRequest
        :return: 結果
        :rtype: gs2_lock_client.control.GetLockPoolStatusResult.GetLockPoolStatusResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.GetLockPoolStatusRequest import GetLockPoolStatusRequest

        from gs2_lock_client.control.GetLockPoolStatusResult import GetLockPoolStatusResult
        return GetLockPoolStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "/status",
            service=self.ENDPOINT,
            component=GetLockPoolStatusRequest.Constant.MODULE,
            target_function=GetLockPoolStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_lock_pool(self, request):
        """
        ロックプールを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_lock_client.control.UpdateLockPoolRequest.UpdateLockPoolRequest
        :return: 結果
        :rtype: gs2_lock_client.control.UpdateLockPoolResult.UpdateLockPoolResult
        """
        body = { 
            "serviceClass": request.get_service_class(),
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.UpdateLockPoolRequest import UpdateLockPoolRequest
        from gs2_lock_client.control.UpdateLockPoolResult import UpdateLockPoolResult
        return UpdateLockPoolResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "",
            service=self.ENDPOINT,
            component=UpdateLockPoolRequest.Constant.MODULE,
            target_function=UpdateLockPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def lock(self, request):
        """
        ロックを取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_lock_client.control.LockRequest.LockRequest
        :return: 結果
        :rtype: gs2_lock_client.control.LockResult.LockResult
        """
        query_strings = {
            'ttl': request.get_ttl(),
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.LockRequest import LockRequest

        from gs2_lock_client.control.LockResult import LockResult
        return LockResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "/lock/transaction/" + str(("null" if request.get_transaction_id() is None or request.get_transaction_id() == "" else request.get_transaction_id())) + "/resource/" + str(("null" if request.get_resource_name() is None or request.get_resource_name() == "" else request.get_resource_name())) + "",
            service=self.ENDPOINT,
            component=LockRequest.Constant.MODULE,
            target_function=LockRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def lock_by_user(self, request):
        """
        ロックを取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_lock_client.control.LockByUserRequest.LockByUserRequest
        :return: 結果
        :rtype: gs2_lock_client.control.LockByUserResult.LockByUserResult
        """
        query_strings = {
            'ttl': request.get_ttl(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.LockByUserRequest import LockByUserRequest

        from gs2_lock_client.control.LockByUserResult import LockByUserResult
        return LockByUserResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "/lock/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "/transaction/" + str(("null" if request.get_transaction_id() is None or request.get_transaction_id() == "" else request.get_transaction_id())) + "/resource/" + str(("null" if request.get_resource_name() is None or request.get_resource_name() == "" else request.get_resource_name())) + "",
            service=self.ENDPOINT,
            component=LockByUserRequest.Constant.MODULE,
            target_function=LockByUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def unlock(self, request):
        """
        アンロックします。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_lock_client.control.UnlockRequest.UnlockRequest
        """
        query_strings = {}
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.UnlockRequest import UnlockRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "/lock/transaction/" + str(("null" if request.get_transaction_id() is None or request.get_transaction_id() == "" else request.get_transaction_id())) + "/resource/" + str(("null" if request.get_resource_name() is None or request.get_resource_name() == "" else request.get_resource_name())) + "",
            service=self.ENDPOINT,
            component=UnlockRequest.Constant.MODULE,
            target_function=UnlockRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def unlock_by_user(self, request):
        """
        アンロックします。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_lock_client.control.UnlockByUserRequest.UnlockByUserRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.UnlockByUserRequest import UnlockByUserRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "/lock/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "/transaction/" + str(("null" if request.get_transaction_id() is None or request.get_transaction_id() == "" else request.get_transaction_id())) + "/resource/" + str(("null" if request.get_resource_name() is None or request.get_resource_name() == "" else request.get_resource_name())) + "",
            service=self.ENDPOINT,
            component=UnlockByUserRequest.Constant.MODULE,
            target_function=UnlockByUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def unlock_force_by_user(self, request):
        """
        強制的にアンロックします。<br>
        <br>
        このAPIを利用すると、トランザクションやロックカウンターの状態を無視して強制的にアンロック出来ます。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_lock_client.control.UnlockForceByUserRequest.UnlockForceByUserRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_lock_client.control.UnlockForceByUserRequest import UnlockForceByUserRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lockPool/" + str(("null" if request.get_lock_pool_name() is None or request.get_lock_pool_name() == "" else request.get_lock_pool_name())) + "/lock/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else request.get_user_id())) + "/resource/" + str(("null" if request.get_resource_name() is None or request.get_resource_name() == "" else request.get_resource_name())) + "",
            service=self.ENDPOINT,
            component=UnlockForceByUserRequest.Constant.MODULE,
            target_function=UnlockForceByUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

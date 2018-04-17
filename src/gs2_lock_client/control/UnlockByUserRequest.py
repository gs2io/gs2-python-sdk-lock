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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_lock_client.Gs2Lock import Gs2Lock


class UnlockByUserRequest(Gs2BasicRequest):

    class Constant(Gs2Lock):
        FUNCTION = "UnlockByUser"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UnlockByUserRequest, self).__init__(params)
        if params is None:
            self.__lock_pool_name = None
        else:
            self.set_lock_pool_name(params['lockPoolName'] if 'lockPoolName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__transaction_id = None
        else:
            self.set_transaction_id(params['transactionId'] if 'transactionId' in params.keys() else None)
        if params is None:
            self.__resource_name = None
        else:
            self.set_resource_name(params['resourceName'] if 'resourceName' in params.keys() else None)

    def get_lock_pool_name(self):
        """
        ロックプールの名前を指定します。を取得
        :return: ロックプールの名前を指定します。
        :rtype: unicode
        """
        return self.__lock_pool_name

    def set_lock_pool_name(self, lock_pool_name):
        """
        ロックプールの名前を指定します。を設定
        :param lock_pool_name: ロックプールの名前を指定します。
        :type lock_pool_name: unicode
        """
        if lock_pool_name and not (isinstance(lock_pool_name, str) or isinstance(lock_pool_name, unicode)):
            raise TypeError(type(lock_pool_name))
        self.__lock_pool_name = lock_pool_name

    def with_lock_pool_name(self, lock_pool_name):
        """
        ロックプールの名前を指定します。を設定
        :param lock_pool_name: ロックプールの名前を指定します。
        :type lock_pool_name: unicode
        :return: this
        :rtype: UnlockByUserRequest
        """
        self.set_lock_pool_name(lock_pool_name)
        return self

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        :return: this
        :rtype: UnlockByUserRequest
        """
        self.set_user_id(user_id)
        return self

    def get_transaction_id(self):
        """
        トランザクションIDを取得
        :return: トランザクションID
        :rtype: unicode
        """
        return self.__transaction_id

    def set_transaction_id(self, transaction_id):
        """
        トランザクションIDを設定
        :param transaction_id: トランザクションID
        :type transaction_id: unicode
        """
        if transaction_id and not (isinstance(transaction_id, str) or isinstance(transaction_id, unicode)):
            raise TypeError(type(transaction_id))
        self.__transaction_id = transaction_id

    def with_transaction_id(self, transaction_id):
        """
        トランザクションIDを設定
        :param transaction_id: トランザクションID
        :type transaction_id: unicode
        :return: this
        :rtype: UnlockByUserRequest
        """
        self.set_transaction_id(transaction_id)
        return self

    def get_resource_name(self):
        """
        ロック解除するリソースの名前を取得
        :return: ロック解除するリソースの名前
        :rtype: unicode
        """
        return self.__resource_name

    def set_resource_name(self, resource_name):
        """
        ロック解除するリソースの名前を設定
        :param resource_name: ロック解除するリソースの名前
        :type resource_name: unicode
        """
        if resource_name and not (isinstance(resource_name, str) or isinstance(resource_name, unicode)):
            raise TypeError(type(resource_name))
        self.__resource_name = resource_name

    def with_resource_name(self, resource_name):
        """
        ロック解除するリソースの名前を設定
        :param resource_name: ロック解除するリソースの名前
        :type resource_name: unicode
        :return: this
        :rtype: UnlockByUserRequest
        """
        self.set_resource_name(resource_name)
        return self

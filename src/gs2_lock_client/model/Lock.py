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

class Lock(object):

    def __init__(self, params=None):
        if params is None:
            self.__lock_id = None
            self.__lock_pool_id = None
            self.__user_id = None
            self.__transaction_id = None
            self.__resource_name = None
            self.__ttl = None
        else:
            self.set_lock_id(params['lockId'] if 'lockId' in params.keys() else None)
            self.set_lock_pool_id(params['lockPoolId'] if 'lockPoolId' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_transaction_id(params['transactionId'] if 'transactionId' in params.keys() else None)
            self.set_resource_name(params['resourceName'] if 'resourceName' in params.keys() else None)
            self.set_ttl(params['ttl'] if 'ttl' in params.keys() else None)


    def get_lock_id(self):
        """
        ロックIDを取得
        :return: ロックID
        :rtype: unicode
        """
        return self.__lock_id

    def set_lock_id(self, lock_id):
        """
        ロックIDを設定
        :param lock_id: ロックID
        :type lock_id: unicode
        """
        self.__lock_id = lock_id

    def get_lock_pool_id(self):
        """
        ロックプールGRNを取得
        :return: ロックプールGRN
        :rtype: unicode
        """
        return self.__lock_pool_id

    def set_lock_pool_id(self, lock_pool_id):
        """
        ロックプールGRNを設定
        :param lock_pool_id: ロックプールGRN
        :type lock_pool_id: unicode
        """
        self.__lock_pool_id = lock_pool_id

    def get_user_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        オーナーIDを設定
        :param user_id: オーナーID
        :type user_id: unicode
        """
        self.__user_id = user_id

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
        self.__transaction_id = transaction_id

    def get_resource_name(self):
        """
        リソース名を取得
        :return: リソース名
        :rtype: unicode
        """
        return self.__resource_name

    def set_resource_name(self, resource_name):
        """
        リソース名を設定
        :param resource_name: リソース名
        :type resource_name: unicode
        """
        self.__resource_name = resource_name

    def get_ttl(self):
        """
        有効期限を取得
        :return: 有効期限
        :rtype: int
        """
        return self.__ttl

    def set_ttl(self, ttl):
        """
        有効期限を設定
        :param ttl: 有効期限
        :type ttl: int
        """
        self.__ttl = ttl

    def to_dict(self):
        return { 
            "lockId": self.__lock_id,
            "lockPoolId": self.__lock_pool_id,
            "userId": self.__user_id,
            "transactionId": self.__transaction_id,
            "resourceName": self.__resource_name,
            "ttl": self.__ttl,
        }
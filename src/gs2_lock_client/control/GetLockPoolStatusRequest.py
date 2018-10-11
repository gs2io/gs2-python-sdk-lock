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


class GetLockPoolStatusRequest(Gs2BasicRequest):

    class Constant(Gs2Lock):
        FUNCTION = "GetLockPoolStatus"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetLockPoolStatusRequest, self).__init__(params)
        if params is None:
            self.__lock_pool_name = None
        else:
            self.set_lock_pool_name(params['lockPoolName'] if 'lockPoolName' in params.keys() else None)

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
        if lock_pool_name is not None and not (isinstance(lock_pool_name, str) or isinstance(lock_pool_name, unicode)):
            raise TypeError(type(lock_pool_name))
        self.__lock_pool_name = lock_pool_name

    def with_lock_pool_name(self, lock_pool_name):
        """
        ロックプールの名前を指定します。を設定
        :param lock_pool_name: ロックプールの名前を指定します。
        :type lock_pool_name: unicode
        :return: this
        :rtype: GetLockPoolStatusRequest
        """
        self.set_lock_pool_name(lock_pool_name)
        return self

# Copyright 2013-2021 Software Radio Systems Limited
#
# This file is part of CoreScope.
#
# CoreScope is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# CoreScope is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# A copy of the GNU Affero General Public License can be found in
# the LICENSE file in the top-level directory of this distribution
# and at http://www.gnu.org/licenses/.
#

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.statusenum_string import STATUSENUMString
from ..types import UNSET, Unset

T = TypeVar("T", bound="DtoNgapStatus")


@attr.s(auto_attribs=True)
class DtoNgapStatus:
    """ """

    ngap_status: Union[Unset, STATUSENUMString] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ngap_status: Union[Unset, str] = UNSET
        if not isinstance(self.ngap_status, Unset):
            ngap_status = self.ngap_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ngap_status is not UNSET:
            field_dict["ngap_status"] = ngap_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ngap_status = d.pop("ngap_status", UNSET)
        ngap_status: Union[Unset, STATUSENUMString]
        if isinstance(_ngap_status, Unset):
            ngap_status = UNSET
        else:
            ngap_status = STATUSENUMString(_ngap_status)

        dto_ngap_status = cls(
            ngap_status=ngap_status,
        )

        dto_ngap_status.additional_properties = d
        return dto_ngap_status

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
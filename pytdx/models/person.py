from typing import Optional, List, Dict
from .base_model import BaseModel


class OrgApplication(BaseModel):
    def __init__(
        self,
        SecurityRoleId: Optional[str] = None,
        SecurityRoleName: Optional[str] = None,
        IsAdministrator: Optional[bool] = None,
        ID: Optional[int] = None,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        SystemClass: Optional[str] = None,
        IsDefault: Optional[bool] = None,
        IsActive: Optional[bool] = None,
    ):
        self.SecurityRoleId = SecurityRoleId
        self.SecurityRoleName = SecurityRoleName
        self.IsAdministrator = IsAdministrator
        self.ID = ID
        self.Name = Name
        self.Description = Description
        self.SystemClass = SystemClass
        self.IsDefault = IsDefault
        self.IsActive = IsActive


class Person(BaseModel):
    def __init__(
        self,
        UID: Optional[str] = None,
        ReferenceID: Optional[int] = None,
        BEID: Optional[str] = None,
        BEIDInt: Optional[int] = None,
        IsActive: Optional[bool] = None,
        IsConfidential: Optional[bool] = None,
        UserName: Optional[str] = None,
        FullName: Optional[str] = None,
        FirstName: Optional[str] = None,
        LastName: Optional[str] = None,
        MiddleName: Optional[str] = None,
        Salutation: Optional[str] = None,
        Nickname: Optional[str] = None,
        DefaultAccountID: Optional[int] = None,
        DefaultAccountName: Optional[str] = None,
        PrimaryEmail: Optional[str] = None,
        AlternateEmail: Optional[str] = None,
        ExternalID: Optional[str] = None,
        AlternateID: Optional[str] = None,
        Applications: Optional[List[str]] = None,
        SecurityRoleName: Optional[str] = None,
        SecurityRoleID: Optional[str] = None,
        Permissions: Optional[List[str]] = None,
        OrgApplications: Optional[List[OrgApplication]] = None,
        PrimaryClientPortalApplicationID: Optional[any] = None,
        GroupIDs: Optional[List[int]] = None,
        AlertEmail: Optional[str] = None,
        ProfileImageFileName: Optional[str] = None,
        Company: Optional[str] = None,
        Title: Optional[str] = None,
        HomePhone: Optional[str] = None,
        PrimaryPhone: Optional[str] = None,
        WorkPhone: Optional[str] = None,
        Pager: Optional[str] = None,
        OtherPhone: Optional[str] = None,
        MobilePhone: Optional[str] = None,
        Fax: Optional[str] = None,
        DefaultPriorityID: Optional[int] = None,
        DefaultPriorityName: Optional[str] = None,
        AboutMe: Optional[str] = None,
        WorkAddress: Optional[str] = None,
        WorkCity: Optional[str] = None,
        WorkState: Optional[str] = None,
        WorkZip: Optional[str] = None,
        WorkCountry: Optional[str] = None,
        HomeAddress: Optional[str] = None,
        HomeCity: Optional[str] = None,
        HomeState: Optional[str] = None,
        HomeZip: Optional[str] = None,
        HomeCountry: Optional[str] = None,
        LocationID: Optional[int] = None,
        LocationName: Optional[str] = None,
        LocationRoomID: Optional[int] = None,
        LocationRoomName: Optional[str] = None,
        DefaultRate: Optional[float] = None,
        CostRate: Optional[float] = None,
        IsEmployee: Optional[bool] = None,
        WorkableHours: Optional[float] = None,
        IsCapacityManaged: Optional[bool] = None,
        ReportTimeAfterDate: Optional[str] = None,
        EndDate: Optional[str] = None,
        ShouldReportTime: Optional[bool] = None,
        ReportsToUID: Optional[str] = None,
        ReportsToFullName: Optional[str] = None,
        ResourcePoolID: Optional[int] = None,
        ResourcePoolName: Optional[str] = None,
        TZID: Optional[int] = None,
        TZName: Optional[str] = None,
        TypeID: Optional[int] = None,
        AuthenticationUserName: Optional[str] = None,
        AuthenticationProviderID: Optional[int] = None,
        Attributes: Optional[List[Dict[str, any]]] = None,
        IMProvider: Optional[str] = None,
        IMHandle: Optional[str] = None,
    ):
        self.UID = UID
        self.ReferenceID = ReferenceID
        self.BEID = BEID
        self.BEIDInt = BEIDInt
        self.IsActive = IsActive
        self.IsConfidential = IsConfidential
        self.UserName = UserName
        self.FullName = FullName
        self.FirstName = FirstName
        self.LastName = LastName
        self.MiddleName = MiddleName
        self.Salutation = Salutation
        self.Nickname = Nickname
        self.DefaultAccountID = DefaultAccountID
        self.DefaultAccountName = DefaultAccountName
        self.PrimaryEmail = PrimaryEmail
        self.AlternateEmail = AlternateEmail
        self.ExternalID = ExternalID
        self.AlternateID = AlternateID
        self.Applications = Applications
        self.SecurityRoleName = SecurityRoleName
        self.SecurityRoleID = SecurityRoleID
        self.Permissions = Permissions
        self.OrgApplications = OrgApplications
        self.PrimaryClientPortalApplicationID = PrimaryClientPortalApplicationID
        self.GroupIDs = GroupIDs
        self.AlertEmail = AlertEmail
        self.ProfileImageFileName = ProfileImageFileName
        self.Company = Company
        self.Title = Title
        self.HomePhone = HomePhone
        self.PrimaryPhone = PrimaryPhone
        self.WorkPhone = WorkPhone
        self.Pager = Pager
        self.OtherPhone = OtherPhone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.DefaultPriorityID = DefaultPriorityID
        self.DefaultPriorityName = DefaultPriorityName
        self.AboutMe = AboutMe
        self.WorkAddress = WorkAddress
        self.WorkCity = WorkCity
        self.WorkState = WorkState
        self.WorkZip = WorkZip
        self.WorkCountry = WorkCountry
        self.HomeAddress = HomeAddress
        self.HomeCity = HomeCity
        self.HomeState = HomeState
        self.HomeZip = HomeZip
        self.HomeCountry = HomeCountry
        self.LocationID = LocationID
        self.LocationName = LocationName
        self.LocationRoomID = LocationRoomID
        self.LocationRoomName = LocationRoomName
        self.DefaultRate = DefaultRate
        self.CostRate = CostRate
        self.IsEmployee = IsEmployee
        self.WorkableHours = WorkableHours
        self.IsCapacityManaged = IsCapacityManaged
        self.ReportTimeAfterDate = ReportTimeAfterDate
        self.EndDate = EndDate
        self.ShouldReportTime = ShouldReportTime
        self.ReportsToUID = ReportsToUID
        self.ReportsToFullName = ReportsToFullName
        self.ResourcePoolID = ResourcePoolID
        self.ResourcePoolName = ResourcePoolName
        self.TZID = TZID
        self.TZName = TZName
        self.TypeID = TypeID
        self.AuthenticationUserName = AuthenticationUserName
        self.AuthenticationProviderID = AuthenticationProviderID
        self.Attributes = Attributes
        self.IMProvider = IMProvider
        self.IMHandle = IMHandle

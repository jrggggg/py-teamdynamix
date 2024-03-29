from typing import Optional, List
from .base_model import BaseModel


class NotifyItem(BaseModel):
    def __init__(
        self,
        ItemRole: Optional[str] = None,
        Name: Optional[str] = None,
        Initials: Optional[str] = None,
        Value: Optional[str] = None,
        RefValue: Optional[int] = None,
        ProfileImageFileName: Optional[str] = None,
    ):
        self.ItemRole = ItemRole
        self.Name = Name
        self.Initials = Initials
        self.Value = Value
        self.RefValue = RefValue
        self.ProfileImageFileName = ProfileImageFileName


class AttributeItem(BaseModel):
    def __init__(
        self,
        ID: Optional[int] = None,
        Name: Optional[str] = None,
        Order: Optional[int] = None,
        Description: Optional[str] = None,
        SectionID: Optional[int] = None,
        SectionName: Optional[str] = None,
        FieldType: Optional[str] = None,
        DataType: Optional[str] = None,
        Choices: Optional[List[str]] = None,
        IsRequired: Optional[bool] = None,
        IsUpdatable: Optional[bool] = None,
        Value: Optional[str] = None,
        ValueText: Optional[str] = None,
        ChoicesText: Optional[str] = None,
        AssociatedItemIDs: Optional[List[int]] = None,
    ):
        self.ID = ID
        self.Name = Name
        self.Order = Order
        self.Description = Description
        self.SectionID = SectionID
        self.SectionName = SectionName
        self.FieldType = FieldType
        self.DataType = DataType
        self.Choices = Choices
        self.IsRequired = IsRequired
        self.IsUpdatable = IsUpdatable
        self.Value = Value
        self.ValueText = ValueText
        self.ChoicesText = ChoicesText
        self.AssociatedItemIDs = AssociatedItemIDs


class Ticket(BaseModel):
    def __init__(
        self,
        ID: Optional[int] = None,
        ParentID: Optional[int] = None,
        ParentTitle: Optional[str] = None,
        ParentClass: Optional[int] = None,
        TypeID: Optional[int] = None,
        TypeName: Optional[str] = None,
        TypeCategoryID: Optional[int] = None,
        TypeCategoryName: Optional[str] = None,
        Classification: Optional[int] = None,
        ClassificationName: Optional[str] = None,
        FormID: Optional[int] = None,
        FormName: Optional[str] = None,
        Title: Optional[str] = None,
        Description: Optional[str] = None,
        IsRichHtml: Optional[bool] = None,
        Uri: Optional[str] = None,
        AccountID: Optional[int] = None,
        AccountName: Optional[str] = None,
        SourceID: Optional[int] = None,
        SourceName: Optional[str] = None,
        StatusID: Optional[int] = None,
        StatusName: Optional[str] = None,
        StatusClass: Optional[int] = None,
        ImpactID: Optional[int] = None,
        ImpactName: Optional[str] = None,
        UrgencyID: Optional[int] = None,
        UrgencyName: Optional[str] = None,
        PriorityID: Optional[int] = None,
        PriorityName: Optional[str] = None,
        PriorityOrder: Optional[float] = None,
        SlaID: Optional[int] = None,
        SlaName: Optional[str] = None,
        IsSlaViolated: Optional[bool] = None,
        IsSlaRespondByViolated: Optional[bool] = None,
        IsSlaResolveByViolated: Optional[bool] = None,
        RespondByDate: Optional[str] = None,
        ResolveByDate: Optional[str] = None,
        SlaBeginDate: Optional[str] = None,
        IsOnHold: Optional[bool] = None,
        PlacedOnHoldDate: Optional[str] = None,
        GoesOffHoldDate: Optional[str] = None,
        CreatedDate: Optional[str] = None,
        CreatedUid: Optional[str] = None,
        CreatedFullName: Optional[str] = None,
        CreatedEmail: Optional[str] = None,
        ModifiedDate: Optional[str] = None,
        ModifiedUid: Optional[str] = None,
        ModifiedFullName: Optional[str] = None,
        RequestorName: Optional[str] = None,
        RequestorFirstName: Optional[str] = None,
        RequestorLastName: Optional[str] = None,
        RequestorEmail: Optional[str] = None,
        RequestorPhone: Optional[str] = None,
        RequestorUid: Optional[str] = None,
        ActualMinutes: Optional[int] = None,
        EstimatedMinutes: Optional[int] = None,
        DaysOld: Optional[int] = None,
        StartDate: Optional[str] = None,
        EndDate: Optional[str] = None,
        ResponsibleUid: Optional[str] = None,
        ResponsibleFullName: Optional[str] = None,
        ResponsibleEmail: Optional[str] = None,
        ResponsibleGroupID: Optional[int] = None,
        ResponsibleGroupName: Optional[str] = None,
        RespondedDate: Optional[str] = None,
        RespondedUid: Optional[str] = None,
        RespondedFullName: Optional[str] = None,
        CompletedDate: Optional[str] = None,
        CompletedUid: Optional[str] = None,
        CompletedFullName: Optional[str] = None,
        ReviewerUid: Optional[str] = None,
        ReviewerFullName: Optional[str] = None,
        ReviewerEmail: Optional[str] = None,
        ReviewingGroupID: Optional[int] = None,
        ReviewingGroupName: Optional[str] = None,
        TimeBudget: Optional[float] = None,
        ExpensesBudget: Optional[float] = None,
        TimeBudgetUsed: Optional[float] = None,
        ExpensesBudgetUsed: Optional[float] = None,
        IsConvertedToTask: Optional[bool] = None,
        ConvertedToTaskDate: Optional[str] = None,
        ConvertedToTaskUid: Optional[str] = None,
        ConvertedToTaskFullName: Optional[str] = None,
        TaskProjectID: Optional[int] = None,
        TaskProjectName: Optional[str] = None,
        TaskPlanID: Optional[int] = None,
        TaskPlanName: Optional[str] = None,
        TaskID: Optional[int] = None,
        TaskTitle: Optional[str] = None,
        TaskStartDate: Optional[str] = None,
        TaskEndDate: Optional[str] = None,
        TaskPercentComplete: Optional[int] = None,
        LocationID: Optional[int] = None,
        LocationName: Optional[str] = None,
        LocationRoomID: Optional[int] = None,
        LocationRoomName: Optional[str] = None,
        RefCode: Optional[str] = None,
        ServiceID: Optional[int] = None,
        ServiceName: Optional[str] = None,
        ServiceOfferingID: Optional[int] = None,
        ServiceOfferingName: Optional[str] = None,
        ServiceCategoryID: Optional[int] = None,
        ServiceCategoryName: Optional[str] = None,
        ArticleID: Optional[int] = None,
        ArticleSubject: Optional[str] = None,
        ArticleStatus: Optional[int] = None,
        ArticleCategoryPathNames: Optional[str] = None,
        ArticleAppID: Optional[int] = None,
        ArticleShortcutID: Optional[str] = None,
        AppID: Optional[int] = None,
        Attributes: Optional[List[AttributeItem]] = None,
        Attachments: Optional[List[dict]] = None,
        Tasks: Optional[List[dict]] = None,
        Notify: Optional[List[NotifyItem]] = None,
        WorkflowID: Optional[int] = None,
        WorkflowConfigurationID: Optional[int] = None,
        WorkflowName: Optional[str] = None,
    ):
        self.ID = ID
        self.ParentID = ParentID
        self.ParentTitle = ParentTitle
        self.ParentClass = ParentClass
        self.TypeID = TypeID
        self.TypeName = TypeName
        self.TypeCategoryID = TypeCategoryID
        self.TypeCategoryName = TypeCategoryName
        self.Classification = Classification
        self.ClassificationName = ClassificationName
        self.FormID = FormID
        self.FormName = FormName
        self.Title = Title
        self.Description = Description
        self.IsRichHtml = IsRichHtml
        self.Uri = Uri
        self.AccountID = AccountID
        self.AccountName = AccountName
        self.SourceID = SourceID
        self.SourceName = SourceName
        self.StatusID = StatusID
        self.StatusName = StatusName
        self.StatusClass = StatusClass
        self.ImpactID = ImpactID
        self.ImpactName = ImpactName
        self.UrgencyID = UrgencyID
        self.UrgencyName = UrgencyName
        self.PriorityID = PriorityID
        self.PriorityName = PriorityName
        self.PriorityOrder = PriorityOrder
        self.SlaID = SlaID
        self.SlaName = SlaName
        self.IsSlaViolated = IsSlaViolated
        self.IsSlaRespondByViolated = IsSlaRespondByViolated
        self.IsSlaResolveByViolated = IsSlaResolveByViolated
        self.RespondByDate = RespondByDate
        self.ResolveByDate = ResolveByDate
        self.SlaBeginDate = SlaBeginDate
        self.IsOnHold = IsOnHold
        self.PlacedOnHoldDate = PlacedOnHoldDate
        self.GoesOffHoldDate = GoesOffHoldDate
        self.CreatedDate = CreatedDate
        self.CreatedUid = CreatedUid
        self.CreatedFullName = CreatedFullName
        self.CreatedEmail = CreatedEmail
        self.ModifiedDate = ModifiedDate
        self.ModifiedUid = ModifiedUid
        self.ModifiedFullName = ModifiedFullName
        self.RequestorName = RequestorName
        self.RequestorFirstName = RequestorFirstName
        self.RequestorLastName = RequestorLastName
        self.RequestorEmail = RequestorEmail
        self.RequestorPhone = RequestorPhone
        self.RequestorUid = RequestorUid
        self.ActualMinutes = ActualMinutes
        self.EstimatedMinutes = EstimatedMinutes
        self.DaysOld = DaysOld
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.ResponsibleUid = ResponsibleUid
        self.ResponsibleFullName = ResponsibleFullName
        self.ResponsibleEmail = ResponsibleEmail
        self.ResponsibleGroupID = ResponsibleGroupID
        self.ResponsibleGroupName = ResponsibleGroupName
        self.RespondedDate = RespondedDate
        self.RespondedUid = RespondedUid
        self.RespondedFullName = RespondedFullName
        self.CompletedDate = CompletedDate
        self.CompletedUid = CompletedUid
        self.CompletedFullName = CompletedFullName
        self.ReviewerUid = ReviewerUid
        self.ReviewerFullName = ReviewerFullName
        self.ReviewerEmail = ReviewerEmail
        self.ReviewingGroupID = ReviewingGroupID
        self.ReviewingGroupName = ReviewingGroupName
        self.TimeBudget = TimeBudget
        self.ExpensesBudget = ExpensesBudget
        self.TimeBudgetUsed = TimeBudgetUsed
        self.ExpensesBudgetUsed = ExpensesBudgetUsed
        self.IsConvertedToTask = IsConvertedToTask
        self.ConvertedToTaskDate = ConvertedToTaskDate
        self.ConvertedToTaskUid = ConvertedToTaskUid
        self.ConvertedToTaskFullName = ConvertedToTaskFullName
        self.TaskProjectID = TaskProjectID
        self.TaskProjectName = TaskProjectName
        self.TaskPlanID = TaskPlanID
        self.TaskPlanName = TaskPlanName
        self.TaskID = TaskID
        self.TaskTitle = TaskTitle
        self.TaskStartDate = TaskStartDate
        self.TaskEndDate = TaskEndDate
        self.TaskPercentComplete = TaskPercentComplete
        self.LocationID = LocationID
        self.LocationName = LocationName
        self.LocationRoomID = LocationRoomID
        self.LocationRoomName = LocationRoomName
        self.RefCode = RefCode
        self.ServiceID = ServiceID
        self.ServiceName = ServiceName
        self.ServiceOfferingID = ServiceOfferingID
        self.ServiceOfferingName = ServiceOfferingName
        self.ServiceCategoryID = ServiceCategoryID
        self.ServiceCategoryName = ServiceCategoryName
        self.ArticleID = ArticleID
        self.ArticleSubject = ArticleSubject
        self.ArticleStatus = ArticleStatus
        self.ArticleCategoryPathNames = ArticleCategoryPathNames
        self.ArticleAppID = ArticleAppID
        self.ArticleShortcutID = ArticleShortcutID
        self.AppID = AppID
        self.Attributes = Attributes
        self.Attachments = Attachments
        self.Tasks = Tasks
        self.Notify = Notify
        self.WorkflowID = WorkflowID
        self.WorkflowConfigurationID = WorkflowConfigurationID
        self.WorkflowName = WorkflowName


class TicketFeed(BaseModel):
    def __init__(
        self,
        ID: Optional[int] = None,
        CreatedUid: Optional[str] = None,
        CreatedRefID: Optional[int] = None,
        CreatedFullName: Optional[str] = None,
        CreatedFirstName: Optional[str] = None,
        CreatedLastName: Optional[str] = None,
        CreatedByPicPath: Optional[str] = None,
        CreatedDate: Optional[str] = None,
        LastUpdatedDate: Optional[str] = None,
        ProjectID: Optional[int] = None,
        ProjectName: Optional[str] = None,
        PlanID: Optional[int] = None,
        PlanName: Optional[str] = None,
        ItemType: Optional[int] = None,
        ItemID: Optional[int] = None,
        ItemTitle: Optional[str] = None,
        ReferenceID: Optional[int] = None,
        Body: Optional[str] = None,
        IsRichHtml: Optional[bool] = None,
        UpdateType: Optional[int] = None,
        NotifiedList: Optional[List] = None,
        IsPrivate: Optional[bool] = None,
        IsParent: Optional[bool] = None,
        Replies: Optional[List] = None,
        RepliesCount: Optional[int] = None,
        Likes: Optional[List] = None,
        ILike: Optional[bool] = None,
        LikesCount: Optional[int] = None,
        Participants: Optional[List] = None,
        BreadcrumbsHtml: Optional[str] = None,
        HasAttachment: Optional[bool] = None,
        Uri: Optional[str] = None,
    ):
        self.ID = ID
        self.CreatedUid = CreatedUid
        self.CreatedRefID = CreatedRefID
        self.CreatedFullName = CreatedFullName
        self.CreatedFirstName = CreatedFirstName
        self.CreatedLastName = CreatedLastName
        self.CreatedByPicPath = CreatedByPicPath
        self.CreatedDate = CreatedDate
        self.LastUpdatedDate = LastUpdatedDate
        self.ProjectID = ProjectID
        self.ProjectName = ProjectName
        self.PlanID = PlanID
        self.PlanName = PlanName
        self.ItemType = ItemType
        self.ItemID = ItemID
        self.ItemTitle = ItemTitle
        self.ReferenceID = ReferenceID
        self.Body = Body
        self.IsRichHtml = IsRichHtml
        self.UpdateType = UpdateType
        self.NotifiedList = NotifiedList
        self.IsPrivate = IsPrivate
        self.IsParent = IsParent
        self.Replies = Replies
        self.RepliesCount = RepliesCount
        self.Likes = Likes
        self.ILike = ILike
        self.LikesCount = LikesCount
        self.Participants = Participants
        self.BreadcrumbsHtml = BreadcrumbsHtml
        self.HasAttachment = HasAttachment
        self.Uri = Uri


class TicketType(BaseModel):
    def __init__(
        self,
        ID: Optional[int] = None,
        AppID: Optional[int] = None,
        AppName: Optional[str] = None,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        CategoryID: Optional[int] = None,
        CategoryName: Optional[str] = None,
        FullName: Optional[str] = None,
        IsActive: Optional[bool] = None,
        CreatedDate: Optional[str] = None,
        CreatedByUid: Optional[str] = None,
        ModifiedDate: Optional[str] = None,
        ModifiedByUid: Optional[str] = None,
        ReviewerUid: Optional[str] = None,
        ReviewerFullName: Optional[str] = None,
        ReviewerEmail: Optional[str] = None,
        ReviewingGroupID: Optional[int] = None,
        ReviewingGroupName: Optional[str] = None,
        NotifyReviewer: Optional[bool] = None,
        OtherNotificationEmailAddresses: Optional[str] = None,
        DefaultSLAID: Optional[int] = None,
        DefaultSLAName: Optional[str] = None,
        DefaultSLAIsActive: Optional[bool] = None,
        WorkspaceID: Optional[int] = None,
        WorkspaceName: Optional[str] = None,
        ShouldAlertResponsibleOnTaskClose: Optional[bool] = None,
    ):
        self.ID = ID
        self.AppID = AppID
        self.AppName = AppName
        self.Name = Name
        self.Description = Description
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
        self.FullName = FullName
        self.IsActive = IsActive
        self.CreatedDate = CreatedDate
        self.CreatedByUid = CreatedByUid
        self.ModifiedDate = ModifiedDate
        self.ModifiedByUid = ModifiedByUid
        self.ReviewerUid = ReviewerUid
        self.ReviewerFullName = ReviewerFullName
        self.ReviewerEmail = ReviewerEmail
        self.ReviewingGroupID = ReviewingGroupID
        self.ReviewingGroupName = ReviewingGroupName
        self.NotifyReviewer = NotifyReviewer
        self.OtherNotificationEmailAddresses = OtherNotificationEmailAddresses
        self.DefaultSLAID = DefaultSLAID
        self.DefaultSLAName = DefaultSLAName
        self.DefaultSLAIsActive = DefaultSLAIsActive
        self.WorkspaceID = WorkspaceID
        self.WorkspaceName = WorkspaceName
        self.ShouldAlertResponsibleOnTaskClose = ShouldAlertResponsibleOnTaskClose

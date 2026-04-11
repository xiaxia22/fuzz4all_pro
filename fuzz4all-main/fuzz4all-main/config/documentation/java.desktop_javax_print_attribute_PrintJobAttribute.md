# Interface PrintJobAttribute

**Source:** `java.desktop\javax\print\attribute\PrintJobAttribute.html`

### Class Description

```java
public interface
PrintJobAttribute

extends
Attribute
```

PrintJobAttribute

is a tagging interface which a printing attribute
class implements to indicate the attribute describes the status of a Print
Job or some other characteristic of a Print Job. A Print Service instance
adds a number of

PrintJobAttributes

to a Print Job's attribute set to
report the Print Job's status. If an attribute implements

PrintRequestAttribute

as well as

PrintJobAttribute

, the client may include the attribute in a
attribute set to specify the attribute's value for the Print Job.

**All Superinterfaces:** Attribute

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface PrintJobAttribute

**All Superinterfaces:** Attribute

,

Serializable

**All Known Implementing Classes:** Chromaticity

,

Copies

,

DateTimeAtCompleted

,

DateTimeAtCreation

,

DateTimeAtProcessing

,

Destination

,

Fidelity

,

Finishings

,

JobHoldUntil

,

JobImpressions

,

JobImpressionsCompleted

,

JobKOctets

,

JobKOctetsProcessed

,

JobMediaSheets

,

JobMediaSheetsCompleted

,

JobMessageFromOperator

,

JobName

,

JobOriginatingUserName

,

JobPriority

,

JobSheets

,

JobState

,

JobStateReasons

,

Media

,

MediaName

,

MediaPrintableArea

,

MediaSizeName

,

MediaTray

,

MultipleDocumentHandling

,

NumberOfDocuments

,

NumberOfInterveningJobs

,

NumberUp

,

OrientationRequested

,

OutputDeviceAssigned

,

PageRanges

,

PresentationDirection

,

PrinterResolution

,

PrintQuality

,

SheetCollate

,

Sides

```java
public interface
PrintJobAttribute

extends
Attribute
```

PrintJobAttribute

is a tagging interface which a printing attribute
class implements to indicate the attribute describes the status of a Print
Job or some other characteristic of a Print Job. A Print Service instance
adds a number of

PrintJobAttributes

to a Print Job's attribute set to
report the Print Job's status. If an attribute implements

PrintRequestAttribute

as well as

PrintJobAttribute

, the client may include the attribute in a
attribute set to specify the attribute's value for the Print Job.

**See Also:** PrintRequestAttributeSet

,

PrintJobAttributeSet

public interface

PrintJobAttribute

extends

Attribute

PrintJobAttribute

is a tagging interface which a printing attribute
class implements to indicate the attribute describes the status of a Print
Job or some other characteristic of a Print Job. A Print Service instance
adds a number of

PrintJobAttributes

to a Print Job's attribute set to
report the Print Job's status. If an attribute implements

PrintRequestAttribute

as well as

PrintJobAttribute

, the client may include the attribute in a
attribute set to specify the attribute's value for the Print Job.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

Method Summary

- Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

---

#### Method Summary

Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

---


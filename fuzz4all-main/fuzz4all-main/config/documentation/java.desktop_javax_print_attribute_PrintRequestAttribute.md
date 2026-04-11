# Interface PrintRequestAttribute

**Source:** `java.desktop\javax\print\attribute\PrintRequestAttribute.html`

### Class Description

```java
public interface
PrintRequestAttribute

extends
Attribute
```

Interface

PrintRequestAttribute

is a tagging interface which a
printing attribute class implements to indicate the attribute denotes a
requested setting for a print job.

Attributes which are tagged with

PrintRequestAttribute

and are also
tagged as

PrintJobAttribute

, represent the subset of job attributes
which can be part of the specification of a job request.

If an attribute implements

DocAttribute

as well as

PrintRequestAttribute

, the client may include the attribute in a

Doc

's attribute set to specify a job setting which pertains just to
that doc.

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

#### Interface PrintRequestAttribute

**All Superinterfaces:** Attribute

,

Serializable

**All Known Implementing Classes:** Chromaticity

,

Copies

,

Destination

,

DialogOwner

,

DialogTypeSelection

,

Fidelity

,

Finishings

,

JobHoldUntil

,

JobImpressions

,

JobKOctets

,

JobMediaSheets

,

JobName

,

JobPriority

,

JobSheets

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

NumberUp

,

OrientationRequested

,

PageRanges

,

PresentationDirection

,

PrinterResolution

,

PrintQuality

,

RequestingUserName

,

SheetCollate

,

Sides

```java
public interface
PrintRequestAttribute

extends
Attribute
```

Interface

PrintRequestAttribute

is a tagging interface which a
printing attribute class implements to indicate the attribute denotes a
requested setting for a print job.

Attributes which are tagged with

PrintRequestAttribute

and are also
tagged as

PrintJobAttribute

, represent the subset of job attributes
which can be part of the specification of a job request.

If an attribute implements

DocAttribute

as well as

PrintRequestAttribute

, the client may include the attribute in a

Doc

's attribute set to specify a job setting which pertains just to
that doc.

**See Also:** DocAttributeSet

,

PrintRequestAttributeSet

public interface

PrintRequestAttribute

extends

Attribute

Interface

PrintRequestAttribute

is a tagging interface which a
printing attribute class implements to indicate the attribute denotes a
requested setting for a print job.

Attributes which are tagged with

PrintRequestAttribute

and are also
tagged as

PrintJobAttribute

, represent the subset of job attributes
which can be part of the specification of a job request.

If an attribute implements

DocAttribute

as well as

PrintRequestAttribute

, the client may include the attribute in a

Doc

's attribute set to specify a job setting which pertains just to
that doc.

Attributes which are tagged with

PrintRequestAttribute

and are also
tagged as

PrintJobAttribute

, represent the subset of job attributes
which can be part of the specification of a job request.

If an attribute implements

DocAttribute

as well as

PrintRequestAttribute

, the client may include the attribute in a

Doc

's attribute set to specify a job setting which pertains just to
that doc.

If an attribute implements

DocAttribute

as well as

PrintRequestAttribute

, the client may include the attribute in a

Doc

's attribute set to specify a job setting which pertains just to
that doc.

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


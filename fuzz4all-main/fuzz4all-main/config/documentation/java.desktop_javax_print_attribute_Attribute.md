# Interface Attribute

**Source:** `java.desktop\javax\print\attribute\Attribute.html`

### Class Description

```java
public interface
Attribute

extends
Serializable
```

Interface

Attribute

is the base interface implemented by any and
every printing attribute class to indicate that the class represents a
printing attribute. All printing attributes are serializable.

**All Superinterfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value when it is added to an attribute set.

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### String
getName()

Get the name of the category of which this attribute value is an
instance.

Note:

This method is intended to provide a default, nonlocalized
string for the attribute's category. If two attribute objects return the
same category from the

getCategory()

method, they should return
the same name from the

getName()

method.

**Returns:**
- attribute category name

---

### Additional Sections

#### Interface Attribute

**All Superinterfaces:** Serializable

**All Known Subinterfaces:** DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

,

PrintServiceAttribute

,

SupportedValuesAttribute

**All Known Implementing Classes:** Chromaticity

,

ColorSupported

,

Compression

,

Copies

,

CopiesSupported

,

DateTimeAtCompleted

,

DateTimeAtCreation

,

DateTimeAtProcessing

,

Destination

,

DialogOwner

,

DialogTypeSelection

,

DocumentName

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

JobImpressionsSupported

,

JobKOctets

,

JobKOctetsProcessed

,

JobKOctetsSupported

,

JobMediaSheets

,

JobMediaSheetsCompleted

,

JobMediaSheetsSupported

,

JobMessageFromOperator

,

JobName

,

JobOriginatingUserName

,

JobPriority

,

JobPrioritySupported

,

JobSheets

,

JobState

,

JobStateReason

,

JobStateReasons

,

Media

,

MediaName

,

MediaPrintableArea

,

MediaSize

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

NumberUpSupported

,

OrientationRequested

,

OutputDeviceAssigned

,

PageRanges

,

PagesPerMinute

,

PagesPerMinuteColor

,

PDLOverrideSupported

,

PresentationDirection

,

PrinterInfo

,

PrinterIsAcceptingJobs

,

PrinterLocation

,

PrinterMakeAndModel

,

PrinterMessageFromOperator

,

PrinterMoreInfo

,

PrinterMoreInfoManufacturer

,

PrinterName

,

PrinterResolution

,

PrinterState

,

PrinterStateReason

,

PrinterStateReasons

,

PrinterURI

,

PrintQuality

,

QueuedJobCount

,

ReferenceUriSchemesSupported

,

RequestingUserName

,

Severity

,

SheetCollate

,

Sides

```java
public interface
Attribute

extends
Serializable
```

Interface

Attribute

is the base interface implemented by any and
every printing attribute class to indicate that the class represents a
printing attribute. All printing attributes are serializable.

public interface

Attribute

extends

Serializable

Interface

Attribute

is the base interface implemented by any and
every printing attribute class to indicate that the class represents a
printing attribute. All printing attributes are serializable.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value when it is added to an attribute set.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value when it is added to an attribute set.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

---

#### Method Summary

Get the printing attribute class which is to be used as the "category"
for this printing attribute value when it is added to an attribute set.

Get the name of the category of which this attribute value is an
instance.

============ METHOD DETAIL ==========

- Method Detail

- getCategory

```java
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value when it is added to an attribute set.

**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

Note:

This method is intended to provide a default, nonlocalized
string for the attribute's category. If two attribute objects return the
same category from the

getCategory()

method, they should return
the same name from the

getName()

method.

**Returns:** attribute category name

Method Detail

- getCategory

```java
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value when it is added to an attribute set.

**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

Note:

This method is intended to provide a default, nonlocalized
string for the attribute's category. If two attribute objects return the
same category from the

getCategory()

method, they should return
the same name from the

getName()

method.

**Returns:** attribute category name

---

#### Method Detail

getCategory

```java
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value when it is added to an attribute set.

**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value when it is added to an attribute set.

getName

```java
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

Note:

This method is intended to provide a default, nonlocalized
string for the attribute's category. If two attribute objects return the
same category from the

getCategory()

method, they should return
the same name from the

getName()

method.

**Returns:** attribute category name

---

#### getName

String

getName()

Get the name of the category of which this attribute value is an
instance.

Note:

This method is intended to provide a default, nonlocalized
string for the attribute's category. If two attribute objects return the
same category from the

getCategory()

method, they should return
the same name from the

getName()

method.

Note:

This method is intended to provide a default, nonlocalized
string for the attribute's category. If two attribute objects return the
same category from the

getCategory()

method, they should return
the same name from the

getName()

method.

---


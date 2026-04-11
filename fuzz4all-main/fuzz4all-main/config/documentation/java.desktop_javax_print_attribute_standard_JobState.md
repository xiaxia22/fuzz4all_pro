# Class JobState

**Source:** `java.desktop\javax\print\attribute\standard\JobState.html`

### Class Description

```java
public class
JobState

extends
EnumSyntax

implements
PrintJobAttribute
```

JobState

is a printing attribute class, an enumeration, that
identifies the current state of a print job. Class

JobState

defines
standard job state values. A Print Service implementation only needs to
report those job states which are appropriate for the particular
implementation; it does not have to report every defined job state. The

JobStateReasons

attribute augments the

JobState

attribute to give more detailed information about the job in
the given job state.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

---

### Field Details

#### public static final
JobState
UNKNOWN

The job state is unknown.

---

#### public static final
JobState
PENDING

The job is a candidate to start processing, but is not yet processing.

---

#### public static final
JobState
PENDING_HELD

The job is not a candidate for processing for any number of reasons but
will return to the

PENDING

state as soon as the reasons are no
longer present. The job's

JobStateReasons

attribute must indicate why the job is no longer a candidate for
processing.

---

#### public static final
JobState
PROCESSING

The job is processing. One or more of the following activities is
occurring:

- The job is using, or is attempting to use, one or more purely
software processes that are analyzing, creating, or interpreting a PDL,
etc.

The job is using, or is attempting to use, one or more hardware
devices that are interpreting a PDL, making marks on a medium, and/or
performing finishing, such as stapling, etc.

The printer has made the job ready for printing, but the output
device is not yet printing it, either because the job hasn't reached
the output device or because the job is queued in the output device or
some other spooler, awaiting the output device to print it.

When the job is in the

PROCESSING

state, the entire job state
includes the detailed status represented in the printer's

PrinterState

and

PrinterStateReasons

attributes.

Implementations may, though they need not, include additional values in
the job's

JobStateReasons

attribute to indicate
the progress of the job, such as adding the

JOB_PRINTING

value to
indicate when the output device is actually making marks on paper and/or
the

PROCESSING_TO_STOP_POINT

value to indicate that the printer
is in the process of canceling or aborting the job.

---

#### public static final
JobState
PROCESSING_STOPPED

The job has stopped while processing for any number of reasons and will
return to the

PROCESSING

state as soon as the reasons are no
longer present.

The job's

JobStateReasons

attribute may indicate
why the job has stopped processing. For example, if the output device is
stopped, the

PRINTER_STOPPED

value may be included in the job's

JobStateReasons

attribute.

Note:

When an output device is stopped, the device usually
indicates its condition in human readable form locally at the device. A
client can obtain more complete device status remotely by querying the
printer's

PrinterState

and

PrinterStateReasons

attributes.

---

#### public static final
JobState
CANCELED

The job has been canceled by some human agency, the printer has completed
canceling the job, and all job status attributes have reached their final
values for the job. While the printer is canceling the job, the job
remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

value and one of the

CANCELED_BY_USER

,

CANCELED_BY_OPERATOR

, or

CANCELED_AT_DEVICE

values. When the job moves to the

CANCELED

state, the

PROCESSING_TO_STOP_POINT

value, if
present, must be removed, but the CANCELED_BY_

xxx

value, if
present, must remain.

---

#### public static final
JobState
ABORTED

The job has been aborted by the system (usually while the job was in the

PROCESSING

or

PROCESSING_STOPPED

state), the printer has
completed aborting the job, and all job status attributes have reached
their final values for the job. While the printer is aborting the job,
the job remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

and

ABORTED_BY_SYSTEM

values.
When the job moves to the

ABORTED

state, the

PROCESSING_TO_STOP_POINT

value, if present, must be removed, but
the

ABORTED_BY_SYSTEM

value, if present, must remain.

---

#### public static final
JobState
COMPLETED

The job has completed successfully or with warnings or errors after
processing, all of the job media sheets have been successfully stacked in
the appropriate output bin(s), and all job status attributes have reached
their final values for the job. The job's

JobStateReasons

attribute should contain one of
these values:

COMPLETED_SUCCESSFULLY

,

COMPLETED_WITH_WARNINGS

, or

COMPLETED_WITH_ERRORS

.

---

### Constructor Details

#### protected JobState​(int value)

Construct a new job state enumeration value with the given integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

JobState

.

**Overrides:**
- getStringTable

in class

EnumSyntax

**Returns:**
- the string table

---

#### protected
EnumSyntax
[] getEnumValueTable()

Returns the enumeration value table for class

JobState

.

**Overrides:**
- getEnumValueTable

in class

EnumSyntax

**Returns:**
- the value table

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobState

and any vendor-defined subclasses, the
category is class

JobState

itself.

**Specified by:**
- getCategory

in interface

Attribute

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### public final
String
getName()

Get the name of the category of which this attribute value is an
instance.

For class

JobState

and any vendor-defined subclasses, the
category name is

"job-state"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobState

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.JobState

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.JobState

javax.print.attribute.standard.JobState

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

```java
public class
JobState

extends
EnumSyntax

implements
PrintJobAttribute
```

JobState

is a printing attribute class, an enumeration, that
identifies the current state of a print job. Class

JobState

defines
standard job state values. A Print Service implementation only needs to
report those job states which are appropriate for the particular
implementation; it does not have to report every defined job state. The

JobStateReasons

attribute augments the

JobState

attribute to give more detailed information about the job in
the given job state.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**See Also:** Serialized Form

public class

JobState

extends

EnumSyntax

implements

PrintJobAttribute

JobState

is a printing attribute class, an enumeration, that
identifies the current state of a print job. Class

JobState

defines
standard job state values. A Print Service implementation only needs to
report those job states which are appropriate for the particular
implementation; it does not have to report every defined job state. The

JobStateReasons

attribute augments the

JobState

attribute to give more detailed information about the job in
the given job state.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

JobState

ABORTED

The job has been aborted by the system (usually while the job was in the

PROCESSING

or

PROCESSING_STOPPED

state), the printer has
completed aborting the job, and all job status attributes have reached
their final values for the job.

static

JobState

CANCELED

The job has been canceled by some human agency, the printer has completed
canceling the job, and all job status attributes have reached their final
values for the job.

static

JobState

COMPLETED

The job has completed successfully or with warnings or errors after
processing, all of the job media sheets have been successfully stacked in
the appropriate output bin(s), and all job status attributes have reached
their final values for the job.

static

JobState

PENDING

The job is a candidate to start processing, but is not yet processing.

static

JobState

PENDING_HELD

The job is not a candidate for processing for any number of reasons but
will return to the

PENDING

state as soon as the reasons are no
longer present.

static

JobState

PROCESSING

The job is processing.

static

JobState

PROCESSING_STOPPED

The job has stopped while processing for any number of reasons and will
return to the

PROCESSING

state as soon as the reasons are no
longer present.

static

JobState

UNKNOWN

The job state is unknown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JobState

​(int value)

Construct a new job state enumeration value with the given integer value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

JobState

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

JobState

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

JobState

ABORTED

The job has been aborted by the system (usually while the job was in the

PROCESSING

or

PROCESSING_STOPPED

state), the printer has
completed aborting the job, and all job status attributes have reached
their final values for the job.

static

JobState

CANCELED

The job has been canceled by some human agency, the printer has completed
canceling the job, and all job status attributes have reached their final
values for the job.

static

JobState

COMPLETED

The job has completed successfully or with warnings or errors after
processing, all of the job media sheets have been successfully stacked in
the appropriate output bin(s), and all job status attributes have reached
their final values for the job.

static

JobState

PENDING

The job is a candidate to start processing, but is not yet processing.

static

JobState

PENDING_HELD

The job is not a candidate for processing for any number of reasons but
will return to the

PENDING

state as soon as the reasons are no
longer present.

static

JobState

PROCESSING

The job is processing.

static

JobState

PROCESSING_STOPPED

The job has stopped while processing for any number of reasons and will
return to the

PROCESSING

state as soon as the reasons are no
longer present.

static

JobState

UNKNOWN

The job state is unknown.

---

#### Field Summary

The job has been aborted by the system (usually while the job was in the

PROCESSING

or

PROCESSING_STOPPED

state), the printer has
completed aborting the job, and all job status attributes have reached
their final values for the job.

The job has been canceled by some human agency, the printer has completed
canceling the job, and all job status attributes have reached their final
values for the job.

The job has completed successfully or with warnings or errors after
processing, all of the job media sheets have been successfully stacked in
the appropriate output bin(s), and all job status attributes have reached
their final values for the job.

The job is a candidate to start processing, but is not yet processing.

The job is not a candidate for processing for any number of reasons but
will return to the

PENDING

state as soon as the reasons are no
longer present.

The job is processing.

The job has stopped while processing for any number of reasons and will
return to the

PROCESSING

state as soon as the reasons are no
longer present.

The job state is unknown.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JobState

​(int value)

Construct a new job state enumeration value with the given integer value.

---

#### Constructor Summary

Construct a new job state enumeration value with the given integer value.

Method Summary

All Methods

Instance Methods

Concrete Methods

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
for this printing attribute value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

JobState

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

JobState

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Returns the enumeration value table for class

JobState

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

JobState

.

Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

---

#### Methods declared in class javax.print.attribute. EnumSyntax

Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- UNKNOWN

```java
public static final
JobState
UNKNOWN
```

The job state is unknown.

- PENDING

```java
public static final
JobState
PENDING
```

The job is a candidate to start processing, but is not yet processing.

- PENDING_HELD

```java
public static final
JobState
PENDING_HELD
```

The job is not a candidate for processing for any number of reasons but
will return to the

PENDING

state as soon as the reasons are no
longer present. The job's

JobStateReasons

attribute must indicate why the job is no longer a candidate for
processing.

- PROCESSING

```java
public static final
JobState
PROCESSING
```

The job is processing. One or more of the following activities is
occurring:

- The job is using, or is attempting to use, one or more purely
software processes that are analyzing, creating, or interpreting a PDL,
etc.

The job is using, or is attempting to use, one or more hardware
devices that are interpreting a PDL, making marks on a medium, and/or
performing finishing, such as stapling, etc.

The printer has made the job ready for printing, but the output
device is not yet printing it, either because the job hasn't reached
the output device or because the job is queued in the output device or
some other spooler, awaiting the output device to print it.

When the job is in the

PROCESSING

state, the entire job state
includes the detailed status represented in the printer's

PrinterState

and

PrinterStateReasons

attributes.

Implementations may, though they need not, include additional values in
the job's

JobStateReasons

attribute to indicate
the progress of the job, such as adding the

JOB_PRINTING

value to
indicate when the output device is actually making marks on paper and/or
the

PROCESSING_TO_STOP_POINT

value to indicate that the printer
is in the process of canceling or aborting the job.

- PROCESSING_STOPPED

```java
public static final
JobState
PROCESSING_STOPPED
```

The job has stopped while processing for any number of reasons and will
return to the

PROCESSING

state as soon as the reasons are no
longer present.

The job's

JobStateReasons

attribute may indicate
why the job has stopped processing. For example, if the output device is
stopped, the

PRINTER_STOPPED

value may be included in the job's

JobStateReasons

attribute.

Note:

When an output device is stopped, the device usually
indicates its condition in human readable form locally at the device. A
client can obtain more complete device status remotely by querying the
printer's

PrinterState

and

PrinterStateReasons

attributes.

- CANCELED

```java
public static final
JobState
CANCELED
```

The job has been canceled by some human agency, the printer has completed
canceling the job, and all job status attributes have reached their final
values for the job. While the printer is canceling the job, the job
remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

value and one of the

CANCELED_BY_USER

,

CANCELED_BY_OPERATOR

, or

CANCELED_AT_DEVICE

values. When the job moves to the

CANCELED

state, the

PROCESSING_TO_STOP_POINT

value, if
present, must be removed, but the CANCELED_BY_

xxx

value, if
present, must remain.

- ABORTED

```java
public static final
JobState
ABORTED
```

The job has been aborted by the system (usually while the job was in the

PROCESSING

or

PROCESSING_STOPPED

state), the printer has
completed aborting the job, and all job status attributes have reached
their final values for the job. While the printer is aborting the job,
the job remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

and

ABORTED_BY_SYSTEM

values.
When the job moves to the

ABORTED

state, the

PROCESSING_TO_STOP_POINT

value, if present, must be removed, but
the

ABORTED_BY_SYSTEM

value, if present, must remain.

- COMPLETED

```java
public static final
JobState
COMPLETED
```

The job has completed successfully or with warnings or errors after
processing, all of the job media sheets have been successfully stacked in
the appropriate output bin(s), and all job status attributes have reached
their final values for the job. The job's

JobStateReasons

attribute should contain one of
these values:

COMPLETED_SUCCESSFULLY

,

COMPLETED_WITH_WARNINGS

, or

COMPLETED_WITH_ERRORS

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JobState

```java
protected JobState​(int value)
```

Construct a new job state enumeration value with the given integer value.

**Parameters:** value

- Integer value

============ METHOD DETAIL ==========

- Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

JobState

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

JobState

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobState

and any vendor-defined subclasses, the
category is class

JobState

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

JobState

and any vendor-defined subclasses, the
category name is

"job-state"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- UNKNOWN

```java
public static final
JobState
UNKNOWN
```

The job state is unknown.

- PENDING

```java
public static final
JobState
PENDING
```

The job is a candidate to start processing, but is not yet processing.

- PENDING_HELD

```java
public static final
JobState
PENDING_HELD
```

The job is not a candidate for processing for any number of reasons but
will return to the

PENDING

state as soon as the reasons are no
longer present. The job's

JobStateReasons

attribute must indicate why the job is no longer a candidate for
processing.

- PROCESSING

```java
public static final
JobState
PROCESSING
```

The job is processing. One or more of the following activities is
occurring:

- The job is using, or is attempting to use, one or more purely
software processes that are analyzing, creating, or interpreting a PDL,
etc.

The job is using, or is attempting to use, one or more hardware
devices that are interpreting a PDL, making marks on a medium, and/or
performing finishing, such as stapling, etc.

The printer has made the job ready for printing, but the output
device is not yet printing it, either because the job hasn't reached
the output device or because the job is queued in the output device or
some other spooler, awaiting the output device to print it.

When the job is in the

PROCESSING

state, the entire job state
includes the detailed status represented in the printer's

PrinterState

and

PrinterStateReasons

attributes.

Implementations may, though they need not, include additional values in
the job's

JobStateReasons

attribute to indicate
the progress of the job, such as adding the

JOB_PRINTING

value to
indicate when the output device is actually making marks on paper and/or
the

PROCESSING_TO_STOP_POINT

value to indicate that the printer
is in the process of canceling or aborting the job.

- PROCESSING_STOPPED

```java
public static final
JobState
PROCESSING_STOPPED
```

The job has stopped while processing for any number of reasons and will
return to the

PROCESSING

state as soon as the reasons are no
longer present.

The job's

JobStateReasons

attribute may indicate
why the job has stopped processing. For example, if the output device is
stopped, the

PRINTER_STOPPED

value may be included in the job's

JobStateReasons

attribute.

Note:

When an output device is stopped, the device usually
indicates its condition in human readable form locally at the device. A
client can obtain more complete device status remotely by querying the
printer's

PrinterState

and

PrinterStateReasons

attributes.

- CANCELED

```java
public static final
JobState
CANCELED
```

The job has been canceled by some human agency, the printer has completed
canceling the job, and all job status attributes have reached their final
values for the job. While the printer is canceling the job, the job
remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

value and one of the

CANCELED_BY_USER

,

CANCELED_BY_OPERATOR

, or

CANCELED_AT_DEVICE

values. When the job moves to the

CANCELED

state, the

PROCESSING_TO_STOP_POINT

value, if
present, must be removed, but the CANCELED_BY_

xxx

value, if
present, must remain.

- ABORTED

```java
public static final
JobState
ABORTED
```

The job has been aborted by the system (usually while the job was in the

PROCESSING

or

PROCESSING_STOPPED

state), the printer has
completed aborting the job, and all job status attributes have reached
their final values for the job. While the printer is aborting the job,
the job remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

and

ABORTED_BY_SYSTEM

values.
When the job moves to the

ABORTED

state, the

PROCESSING_TO_STOP_POINT

value, if present, must be removed, but
the

ABORTED_BY_SYSTEM

value, if present, must remain.

- COMPLETED

```java
public static final
JobState
COMPLETED
```

The job has completed successfully or with warnings or errors after
processing, all of the job media sheets have been successfully stacked in
the appropriate output bin(s), and all job status attributes have reached
their final values for the job. The job's

JobStateReasons

attribute should contain one of
these values:

COMPLETED_SUCCESSFULLY

,

COMPLETED_WITH_WARNINGS

, or

COMPLETED_WITH_ERRORS

.

---

#### Field Detail

UNKNOWN

```java
public static final
JobState
UNKNOWN
```

The job state is unknown.

---

#### UNKNOWN

public static final

JobState

UNKNOWN

The job state is unknown.

PENDING

```java
public static final
JobState
PENDING
```

The job is a candidate to start processing, but is not yet processing.

---

#### PENDING

public static final

JobState

PENDING

The job is a candidate to start processing, but is not yet processing.

PENDING_HELD

```java
public static final
JobState
PENDING_HELD
```

The job is not a candidate for processing for any number of reasons but
will return to the

PENDING

state as soon as the reasons are no
longer present. The job's

JobStateReasons

attribute must indicate why the job is no longer a candidate for
processing.

---

#### PENDING_HELD

public static final

JobState

PENDING_HELD

The job is not a candidate for processing for any number of reasons but
will return to the

PENDING

state as soon as the reasons are no
longer present. The job's

JobStateReasons

attribute must indicate why the job is no longer a candidate for
processing.

PROCESSING

```java
public static final
JobState
PROCESSING
```

The job is processing. One or more of the following activities is
occurring:

- The job is using, or is attempting to use, one or more purely
software processes that are analyzing, creating, or interpreting a PDL,
etc.

The job is using, or is attempting to use, one or more hardware
devices that are interpreting a PDL, making marks on a medium, and/or
performing finishing, such as stapling, etc.

The printer has made the job ready for printing, but the output
device is not yet printing it, either because the job hasn't reached
the output device or because the job is queued in the output device or
some other spooler, awaiting the output device to print it.

When the job is in the

PROCESSING

state, the entire job state
includes the detailed status represented in the printer's

PrinterState

and

PrinterStateReasons

attributes.

Implementations may, though they need not, include additional values in
the job's

JobStateReasons

attribute to indicate
the progress of the job, such as adding the

JOB_PRINTING

value to
indicate when the output device is actually making marks on paper and/or
the

PROCESSING_TO_STOP_POINT

value to indicate that the printer
is in the process of canceling or aborting the job.

---

#### PROCESSING

public static final

JobState

PROCESSING

The job is processing. One or more of the following activities is
occurring:

- The job is using, or is attempting to use, one or more purely
software processes that are analyzing, creating, or interpreting a PDL,
etc.

The job is using, or is attempting to use, one or more hardware
devices that are interpreting a PDL, making marks on a medium, and/or
performing finishing, such as stapling, etc.

The printer has made the job ready for printing, but the output
device is not yet printing it, either because the job hasn't reached
the output device or because the job is queued in the output device or
some other spooler, awaiting the output device to print it.

When the job is in the

PROCESSING

state, the entire job state
includes the detailed status represented in the printer's

PrinterState

and

PrinterStateReasons

attributes.

Implementations may, though they need not, include additional values in
the job's

JobStateReasons

attribute to indicate
the progress of the job, such as adding the

JOB_PRINTING

value to
indicate when the output device is actually making marks on paper and/or
the

PROCESSING_TO_STOP_POINT

value to indicate that the printer
is in the process of canceling or aborting the job.

The job is using, or is attempting to use, one or more purely
software processes that are analyzing, creating, or interpreting a PDL,
etc.

The job is using, or is attempting to use, one or more hardware
devices that are interpreting a PDL, making marks on a medium, and/or
performing finishing, such as stapling, etc.

The printer has made the job ready for printing, but the output
device is not yet printing it, either because the job hasn't reached
the output device or because the job is queued in the output device or
some other spooler, awaiting the output device to print it.

Implementations may, though they need not, include additional values in
the job's

JobStateReasons

attribute to indicate
the progress of the job, such as adding the

JOB_PRINTING

value to
indicate when the output device is actually making marks on paper and/or
the

PROCESSING_TO_STOP_POINT

value to indicate that the printer
is in the process of canceling or aborting the job.

PROCESSING_STOPPED

```java
public static final
JobState
PROCESSING_STOPPED
```

The job has stopped while processing for any number of reasons and will
return to the

PROCESSING

state as soon as the reasons are no
longer present.

The job's

JobStateReasons

attribute may indicate
why the job has stopped processing. For example, if the output device is
stopped, the

PRINTER_STOPPED

value may be included in the job's

JobStateReasons

attribute.

Note:

When an output device is stopped, the device usually
indicates its condition in human readable form locally at the device. A
client can obtain more complete device status remotely by querying the
printer's

PrinterState

and

PrinterStateReasons

attributes.

---

#### PROCESSING_STOPPED

public static final

JobState

PROCESSING_STOPPED

The job has stopped while processing for any number of reasons and will
return to the

PROCESSING

state as soon as the reasons are no
longer present.

The job's

JobStateReasons

attribute may indicate
why the job has stopped processing. For example, if the output device is
stopped, the

PRINTER_STOPPED

value may be included in the job's

JobStateReasons

attribute.

Note:

When an output device is stopped, the device usually
indicates its condition in human readable form locally at the device. A
client can obtain more complete device status remotely by querying the
printer's

PrinterState

and

PrinterStateReasons

attributes.

The job's

JobStateReasons

attribute may indicate
why the job has stopped processing. For example, if the output device is
stopped, the

PRINTER_STOPPED

value may be included in the job's

JobStateReasons

attribute.

Note:

When an output device is stopped, the device usually
indicates its condition in human readable form locally at the device. A
client can obtain more complete device status remotely by querying the
printer's

PrinterState

and

PrinterStateReasons

attributes.

Note:

When an output device is stopped, the device usually
indicates its condition in human readable form locally at the device. A
client can obtain more complete device status remotely by querying the
printer's

PrinterState

and

PrinterStateReasons

attributes.

CANCELED

```java
public static final
JobState
CANCELED
```

The job has been canceled by some human agency, the printer has completed
canceling the job, and all job status attributes have reached their final
values for the job. While the printer is canceling the job, the job
remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

value and one of the

CANCELED_BY_USER

,

CANCELED_BY_OPERATOR

, or

CANCELED_AT_DEVICE

values. When the job moves to the

CANCELED

state, the

PROCESSING_TO_STOP_POINT

value, if
present, must be removed, but the CANCELED_BY_

xxx

value, if
present, must remain.

---

#### CANCELED

public static final

JobState

CANCELED

The job has been canceled by some human agency, the printer has completed
canceling the job, and all job status attributes have reached their final
values for the job. While the printer is canceling the job, the job
remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

value and one of the

CANCELED_BY_USER

,

CANCELED_BY_OPERATOR

, or

CANCELED_AT_DEVICE

values. When the job moves to the

CANCELED

state, the

PROCESSING_TO_STOP_POINT

value, if
present, must be removed, but the CANCELED_BY_

xxx

value, if
present, must remain.

ABORTED

```java
public static final
JobState
ABORTED
```

The job has been aborted by the system (usually while the job was in the

PROCESSING

or

PROCESSING_STOPPED

state), the printer has
completed aborting the job, and all job status attributes have reached
their final values for the job. While the printer is aborting the job,
the job remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

and

ABORTED_BY_SYSTEM

values.
When the job moves to the

ABORTED

state, the

PROCESSING_TO_STOP_POINT

value, if present, must be removed, but
the

ABORTED_BY_SYSTEM

value, if present, must remain.

---

#### ABORTED

public static final

JobState

ABORTED

The job has been aborted by the system (usually while the job was in the

PROCESSING

or

PROCESSING_STOPPED

state), the printer has
completed aborting the job, and all job status attributes have reached
their final values for the job. While the printer is aborting the job,
the job remains in its current state, but the job's

JobStateReasons

attribute should contain the

PROCESSING_TO_STOP_POINT

and

ABORTED_BY_SYSTEM

values.
When the job moves to the

ABORTED

state, the

PROCESSING_TO_STOP_POINT

value, if present, must be removed, but
the

ABORTED_BY_SYSTEM

value, if present, must remain.

COMPLETED

```java
public static final
JobState
COMPLETED
```

The job has completed successfully or with warnings or errors after
processing, all of the job media sheets have been successfully stacked in
the appropriate output bin(s), and all job status attributes have reached
their final values for the job. The job's

JobStateReasons

attribute should contain one of
these values:

COMPLETED_SUCCESSFULLY

,

COMPLETED_WITH_WARNINGS

, or

COMPLETED_WITH_ERRORS

.

---

#### COMPLETED

public static final

JobState

COMPLETED

The job has completed successfully or with warnings or errors after
processing, all of the job media sheets have been successfully stacked in
the appropriate output bin(s), and all job status attributes have reached
their final values for the job. The job's

JobStateReasons

attribute should contain one of
these values:

COMPLETED_SUCCESSFULLY

,

COMPLETED_WITH_WARNINGS

, or

COMPLETED_WITH_ERRORS

.

Constructor Detail

- JobState

```java
protected JobState​(int value)
```

Construct a new job state enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

JobState

```java
protected JobState​(int value)
```

Construct a new job state enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### JobState

protected JobState​(int value)

Construct a new job state enumeration value with the given integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

JobState

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

JobState

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobState

and any vendor-defined subclasses, the
category is class

JobState

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

JobState

and any vendor-defined subclasses, the
category name is

"job-state"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

JobState

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

---

#### getStringTable

protected

String

[] getStringTable()

Returns the string table for class

JobState

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

JobState

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

---

#### getEnumValueTable

protected

EnumSyntax

[] getEnumValueTable()

Returns the enumeration value table for class

JobState

.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobState

and any vendor-defined subclasses, the
category is class

JobState

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

public final

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobState

and any vendor-defined subclasses, the
category is class

JobState

itself.

For class

JobState

and any vendor-defined subclasses, the
category is class

JobState

itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

JobState

and any vendor-defined subclasses, the
category name is

"job-state"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### getName

public final

String

getName()

Get the name of the category of which this attribute value is an
instance.

For class

JobState

and any vendor-defined subclasses, the
category name is

"job-state"

.

For class

JobState

and any vendor-defined subclasses, the
category name is

"job-state"

.

---


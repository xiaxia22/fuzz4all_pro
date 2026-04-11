# Class PrinterStateReason

**Source:** `java.desktop\javax\print\attribute\standard\PrinterStateReason.html`

### Class Description

```java
public class
PrinterStateReason

extends
EnumSyntax

implements
Attribute
```

Class

PrinterStateReason

is a printing attribute class, an
enumeration, that provides additional information about the printer's current
state, i.e., information that augments the value of the printer's

PrinterState

attribute. Class PrinterStateReason defines
standard printer state reason values. A Print Service implementation only
needs to report those printer state reasons which are appropriate for the
particular implementation; it does not have to report every defined printer
state reason.

Instances of

PrinterStateReason

do not appear in a Print Service's
attribute set directly. Rather, a

PrinterStateReasons

attribute appears in the
Print Service's attribute set. The

PrinterStateReasons

attribute contains zero, one,
or more than one

PrinterStateReason

objects which pertain to the
Print Service's status, and each PrinterStateReason object is associated with
a

Severity

level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the
corresponding condition becomes true of the printer, and the printer removes
the

PrinterStateReason

object again when the corresponding condition
becomes false, regardless of whether the Print Service's overall

PrinterState

also changed.

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

---

### Field Details

#### public static final
PrinterStateReason
OTHER

The printer has detected an error other than ones listed below.

---

#### public static final
PrinterStateReason
MEDIA_NEEDED

A tray has run out of media.

---

#### public static final
PrinterStateReason
MEDIA_JAM

The device has a media jam.

---

#### public static final
PrinterStateReason
MOVING_TO_PAUSED

Someone has paused the printer, but the device(s) are taking an
appreciable time to stop. Later, when all output has stopped, the

PrinterState

becomes

STOPPED

, and the

PAUSED

value replaces the

MOVING_TO_PAUSED

value in the

PrinterStateReasons

attribute. This value
must be supported if the printer can be paused and the implementation
takes significant time to pause a device in certain circumstances.

---

#### public static final
PrinterStateReason
PAUSED

Someone has paused the printer and the printer's

PrinterState

is

STOPPED

. In this state, a
printer must not produce printed output, but it must perform other
operations requested by a client. If a printer had been printing a job
when the printer was paused, the

Printer

must resume printing
that job when the printer is no longer paused and leave no evidence in
the printed output of such a pause. This value must be supported if the
printer can be paused.

---

#### public static final
PrinterStateReason
SHUTDOWN

Someone has removed a printer from service, and the device may be powered
down or physically removed. In this state, a printer must not produce
printed output, and unless the printer is realized by a print server that
is still active, the printer must perform no other operations requested
by a client. If a printer had been printing a job when it was shut down,
the printer need not resume printing that job when the printer is no
longer shut down. If the printer resumes printing such a job, it may
leave evidence in the printed output of such a shutdown, e.g. the part
printed before the shutdown may be printed a second time after the
shutdown.

---

#### public static final
PrinterStateReason
CONNECTING_TO_DEVICE

The printer has scheduled a job on the output device and is in the
process of connecting to a shared network output device (and might not be
able to actually start printing the job for an arbitrarily long time
depending on the usage of the output device by other servers on the
network).

---

#### public static final
PrinterStateReason
TIMED_OUT

The server was able to connect to the output device (or is always
connected), but was unable to get a response from the output device.

---

#### public static final
PrinterStateReason
STOPPING

The printer is in the process of stopping the device and will be stopped
in a while. When the device is stopped, the printer will change the

PrinterState

to

STOPPED

. The

STOPPING

reason is never an error, even for a printer with a
single output device. When an output device ceases accepting jobs, the
printer's

PrinterStateReasons

will have this
reason while the output device completes printing.

---

#### public static final
PrinterStateReason
STOPPED_PARTLY

When a printer controls more than one output device, this reason
indicates that one or more output devices are stopped. If the reason's
severity is a report, fewer than half of the output devices are stopped.
If the reason's severity is a warning, half or more but fewer than all of
the output devices are stopped.

---

#### public static final
PrinterStateReason
TONER_LOW

The device is low on toner.

---

#### public static final
PrinterStateReason
TONER_EMPTY

The device is out of toner.

---

#### public static final
PrinterStateReason
SPOOL_AREA_FULL

The limit of persistent storage allocated for spooling has been reached.
The printer is temporarily unable to accept more jobs. The printer will
remove this reason when it is able to accept more jobs. This value should
be used by a non-spooling printer that only accepts one or a small number
jobs at a time or a spooling printer that has filled the spool space.

---

#### public static final
PrinterStateReason
COVER_OPEN

One or more covers on the device are open.

---

#### public static final
PrinterStateReason
INTERLOCK_OPEN

One or more interlock devices on the printer are unlocked.

---

#### public static final
PrinterStateReason
DOOR_OPEN

One or more doors on the device are open.

---

#### public static final
PrinterStateReason
INPUT_TRAY_MISSING

One or more input trays are not in the device.

---

#### public static final
PrinterStateReason
MEDIA_LOW

At least one input tray is low on media.

---

#### public static final
PrinterStateReason
MEDIA_EMPTY

At least one input tray is empty.

---

#### public static final
PrinterStateReason
OUTPUT_TRAY_MISSING

One or more output trays are not in the device.

---

#### public static final
PrinterStateReason
OUTPUT_AREA_ALMOST_FULL

One or more output areas are almost full (e.g. tray, stacker, collator).

---

#### public static final
PrinterStateReason
OUTPUT_AREA_FULL

One or more output areas are full (e.g. tray, stacker, collator).

---

#### public static final
PrinterStateReason
MARKER_SUPPLY_LOW

The device is low on at least one marker supply (e.g. toner, ink,
ribbon).

---

#### public static final
PrinterStateReason
MARKER_SUPPLY_EMPTY

The device is out of at least one marker supply (e.g. toner, ink,
ribbon).

---

#### public static final
PrinterStateReason
MARKER_WASTE_ALMOST_FULL

The device marker supply waste receptacle is almost full.

---

#### public static final
PrinterStateReason
MARKER_WASTE_FULL

The device marker supply waste receptacle is full.

---

#### public static final
PrinterStateReason
FUSER_OVER_TEMP

The fuser temperature is above normal.

---

#### public static final
PrinterStateReason
FUSER_UNDER_TEMP

The fuser temperature is below normal.

---

#### public static final
PrinterStateReason
OPC_NEAR_EOL

The optical photo conductor is near end of life.

---

#### public static final
PrinterStateReason
OPC_LIFE_OVER

The optical photo conductor is no longer functioning.

---

#### public static final
PrinterStateReason
DEVELOPER_LOW

The device is low on developer.

---

#### public static final
PrinterStateReason
DEVELOPER_EMPTY

The device is out of developer.

---

#### public static final
PrinterStateReason
INTERPRETER_RESOURCE_UNAVAILABLE

An interpreter resource is unavailable (e.g., font, form).

---

### Constructor Details

#### protected PrinterStateReason​(int value)

Construct a new printer state reason enumeration value with the given
integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

PrinterStateReason

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

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category is class

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category name is

"printer-state-reason"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterStateReason

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.PrinterStateReason

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.PrinterStateReason

javax.print.attribute.standard.PrinterStateReason

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

```java
public class
PrinterStateReason

extends
EnumSyntax

implements
Attribute
```

Class

PrinterStateReason

is a printing attribute class, an
enumeration, that provides additional information about the printer's current
state, i.e., information that augments the value of the printer's

PrinterState

attribute. Class PrinterStateReason defines
standard printer state reason values. A Print Service implementation only
needs to report those printer state reasons which are appropriate for the
particular implementation; it does not have to report every defined printer
state reason.

Instances of

PrinterStateReason

do not appear in a Print Service's
attribute set directly. Rather, a

PrinterStateReasons

attribute appears in the
Print Service's attribute set. The

PrinterStateReasons

attribute contains zero, one,
or more than one

PrinterStateReason

objects which pertain to the
Print Service's status, and each PrinterStateReason object is associated with
a

Severity

level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the
corresponding condition becomes true of the printer, and the printer removes
the

PrinterStateReason

object again when the corresponding condition
becomes false, regardless of whether the Print Service's overall

PrinterState

also changed.

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public class

PrinterStateReason

extends

EnumSyntax

implements

Attribute

Class

PrinterStateReason

is a printing attribute class, an
enumeration, that provides additional information about the printer's current
state, i.e., information that augments the value of the printer's

PrinterState

attribute. Class PrinterStateReason defines
standard printer state reason values. A Print Service implementation only
needs to report those printer state reasons which are appropriate for the
particular implementation; it does not have to report every defined printer
state reason.

Instances of

PrinterStateReason

do not appear in a Print Service's
attribute set directly. Rather, a

PrinterStateReasons

attribute appears in the
Print Service's attribute set. The

PrinterStateReasons

attribute contains zero, one,
or more than one

PrinterStateReason

objects which pertain to the
Print Service's status, and each PrinterStateReason object is associated with
a

Severity

level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the
corresponding condition becomes true of the printer, and the printer removes
the

PrinterStateReason

object again when the corresponding condition
becomes false, regardless of whether the Print Service's overall

PrinterState

also changed.

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

Instances of

PrinterStateReason

do not appear in a Print Service's
attribute set directly. Rather, a

PrinterStateReasons

attribute appears in the
Print Service's attribute set. The

PrinterStateReasons

attribute contains zero, one,
or more than one

PrinterStateReason

objects which pertain to the
Print Service's status, and each PrinterStateReason object is associated with
a

Severity

level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the
corresponding condition becomes true of the printer, and the printer removes
the

PrinterStateReason

object again when the corresponding condition
becomes false, regardless of whether the Print Service's overall

PrinterState

also changed.

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

PrinterStateReason

CONNECTING_TO_DEVICE

The printer has scheduled a job on the output device and is in the
process of connecting to a shared network output device (and might not be
able to actually start printing the job for an arbitrarily long time
depending on the usage of the output device by other servers on the
network).

static

PrinterStateReason

COVER_OPEN

One or more covers on the device are open.

static

PrinterStateReason

DEVELOPER_EMPTY

The device is out of developer.

static

PrinterStateReason

DEVELOPER_LOW

The device is low on developer.

static

PrinterStateReason

DOOR_OPEN

One or more doors on the device are open.

static

PrinterStateReason

FUSER_OVER_TEMP

The fuser temperature is above normal.

static

PrinterStateReason

FUSER_UNDER_TEMP

The fuser temperature is below normal.

static

PrinterStateReason

INPUT_TRAY_MISSING

One or more input trays are not in the device.

static

PrinterStateReason

INTERLOCK_OPEN

One or more interlock devices on the printer are unlocked.

static

PrinterStateReason

INTERPRETER_RESOURCE_UNAVAILABLE

An interpreter resource is unavailable (e.g., font, form).

static

PrinterStateReason

MARKER_SUPPLY_EMPTY

The device is out of at least one marker supply (e.g. toner, ink,
ribbon).

static

PrinterStateReason

MARKER_SUPPLY_LOW

The device is low on at least one marker supply (e.g. toner, ink,
ribbon).

static

PrinterStateReason

MARKER_WASTE_ALMOST_FULL

The device marker supply waste receptacle is almost full.

static

PrinterStateReason

MARKER_WASTE_FULL

The device marker supply waste receptacle is full.

static

PrinterStateReason

MEDIA_EMPTY

At least one input tray is empty.

static

PrinterStateReason

MEDIA_JAM

The device has a media jam.

static

PrinterStateReason

MEDIA_LOW

At least one input tray is low on media.

static

PrinterStateReason

MEDIA_NEEDED

A tray has run out of media.

static

PrinterStateReason

MOVING_TO_PAUSED

Someone has paused the printer, but the device(s) are taking an
appreciable time to stop.

static

PrinterStateReason

OPC_LIFE_OVER

The optical photo conductor is no longer functioning.

static

PrinterStateReason

OPC_NEAR_EOL

The optical photo conductor is near end of life.

static

PrinterStateReason

OTHER

The printer has detected an error other than ones listed below.

static

PrinterStateReason

OUTPUT_AREA_ALMOST_FULL

One or more output areas are almost full (e.g. tray, stacker, collator).

static

PrinterStateReason

OUTPUT_AREA_FULL

One or more output areas are full (e.g. tray, stacker, collator).

static

PrinterStateReason

OUTPUT_TRAY_MISSING

One or more output trays are not in the device.

static

PrinterStateReason

PAUSED

Someone has paused the printer and the printer's

PrinterState

is

STOPPED

.

static

PrinterStateReason

SHUTDOWN

Someone has removed a printer from service, and the device may be powered
down or physically removed.

static

PrinterStateReason

SPOOL_AREA_FULL

The limit of persistent storage allocated for spooling has been reached.

static

PrinterStateReason

STOPPED_PARTLY

When a printer controls more than one output device, this reason
indicates that one or more output devices are stopped.

static

PrinterStateReason

STOPPING

The printer is in the process of stopping the device and will be stopped
in a while.

static

PrinterStateReason

TIMED_OUT

The server was able to connect to the output device (or is always
connected), but was unable to get a response from the output device.

static

PrinterStateReason

TONER_EMPTY

The device is out of toner.

static

PrinterStateReason

TONER_LOW

The device is low on toner.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PrinterStateReason

​(int value)

Construct a new printer state reason enumeration value with the given
integer value.

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

PrinterStateReason

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

PrinterStateReason

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

PrinterStateReason

CONNECTING_TO_DEVICE

The printer has scheduled a job on the output device and is in the
process of connecting to a shared network output device (and might not be
able to actually start printing the job for an arbitrarily long time
depending on the usage of the output device by other servers on the
network).

static

PrinterStateReason

COVER_OPEN

One or more covers on the device are open.

static

PrinterStateReason

DEVELOPER_EMPTY

The device is out of developer.

static

PrinterStateReason

DEVELOPER_LOW

The device is low on developer.

static

PrinterStateReason

DOOR_OPEN

One or more doors on the device are open.

static

PrinterStateReason

FUSER_OVER_TEMP

The fuser temperature is above normal.

static

PrinterStateReason

FUSER_UNDER_TEMP

The fuser temperature is below normal.

static

PrinterStateReason

INPUT_TRAY_MISSING

One or more input trays are not in the device.

static

PrinterStateReason

INTERLOCK_OPEN

One or more interlock devices on the printer are unlocked.

static

PrinterStateReason

INTERPRETER_RESOURCE_UNAVAILABLE

An interpreter resource is unavailable (e.g., font, form).

static

PrinterStateReason

MARKER_SUPPLY_EMPTY

The device is out of at least one marker supply (e.g. toner, ink,
ribbon).

static

PrinterStateReason

MARKER_SUPPLY_LOW

The device is low on at least one marker supply (e.g. toner, ink,
ribbon).

static

PrinterStateReason

MARKER_WASTE_ALMOST_FULL

The device marker supply waste receptacle is almost full.

static

PrinterStateReason

MARKER_WASTE_FULL

The device marker supply waste receptacle is full.

static

PrinterStateReason

MEDIA_EMPTY

At least one input tray is empty.

static

PrinterStateReason

MEDIA_JAM

The device has a media jam.

static

PrinterStateReason

MEDIA_LOW

At least one input tray is low on media.

static

PrinterStateReason

MEDIA_NEEDED

A tray has run out of media.

static

PrinterStateReason

MOVING_TO_PAUSED

Someone has paused the printer, but the device(s) are taking an
appreciable time to stop.

static

PrinterStateReason

OPC_LIFE_OVER

The optical photo conductor is no longer functioning.

static

PrinterStateReason

OPC_NEAR_EOL

The optical photo conductor is near end of life.

static

PrinterStateReason

OTHER

The printer has detected an error other than ones listed below.

static

PrinterStateReason

OUTPUT_AREA_ALMOST_FULL

One or more output areas are almost full (e.g. tray, stacker, collator).

static

PrinterStateReason

OUTPUT_AREA_FULL

One or more output areas are full (e.g. tray, stacker, collator).

static

PrinterStateReason

OUTPUT_TRAY_MISSING

One or more output trays are not in the device.

static

PrinterStateReason

PAUSED

Someone has paused the printer and the printer's

PrinterState

is

STOPPED

.

static

PrinterStateReason

SHUTDOWN

Someone has removed a printer from service, and the device may be powered
down or physically removed.

static

PrinterStateReason

SPOOL_AREA_FULL

The limit of persistent storage allocated for spooling has been reached.

static

PrinterStateReason

STOPPED_PARTLY

When a printer controls more than one output device, this reason
indicates that one or more output devices are stopped.

static

PrinterStateReason

STOPPING

The printer is in the process of stopping the device and will be stopped
in a while.

static

PrinterStateReason

TIMED_OUT

The server was able to connect to the output device (or is always
connected), but was unable to get a response from the output device.

static

PrinterStateReason

TONER_EMPTY

The device is out of toner.

static

PrinterStateReason

TONER_LOW

The device is low on toner.

---

#### Field Summary

The printer has scheduled a job on the output device and is in the
process of connecting to a shared network output device (and might not be
able to actually start printing the job for an arbitrarily long time
depending on the usage of the output device by other servers on the
network).

One or more covers on the device are open.

The device is out of developer.

The device is low on developer.

One or more doors on the device are open.

The fuser temperature is above normal.

The fuser temperature is below normal.

One or more input trays are not in the device.

One or more interlock devices on the printer are unlocked.

An interpreter resource is unavailable (e.g., font, form).

The device is out of at least one marker supply (e.g. toner, ink,
ribbon).

The device is low on at least one marker supply (e.g. toner, ink,
ribbon).

The device marker supply waste receptacle is almost full.

The device marker supply waste receptacle is full.

At least one input tray is empty.

The device has a media jam.

At least one input tray is low on media.

A tray has run out of media.

Someone has paused the printer, but the device(s) are taking an
appreciable time to stop.

The optical photo conductor is no longer functioning.

The optical photo conductor is near end of life.

The printer has detected an error other than ones listed below.

One or more output areas are almost full (e.g. tray, stacker, collator).

One or more output areas are full (e.g. tray, stacker, collator).

One or more output trays are not in the device.

Someone has paused the printer and the printer's

PrinterState

is

STOPPED

.

Someone has removed a printer from service, and the device may be powered
down or physically removed.

The limit of persistent storage allocated for spooling has been reached.

When a printer controls more than one output device, this reason
indicates that one or more output devices are stopped.

The printer is in the process of stopping the device and will be stopped
in a while.

The server was able to connect to the output device (or is always
connected), but was unable to get a response from the output device.

The device is out of toner.

The device is low on toner.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PrinterStateReason

​(int value)

Construct a new printer state reason enumeration value with the given
integer value.

---

#### Constructor Summary

Construct a new printer state reason enumeration value with the given
integer value.

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

PrinterStateReason

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

PrinterStateReason

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

PrinterStateReason

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

PrinterStateReason

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

- OTHER

```java
public static final
PrinterStateReason
OTHER
```

The printer has detected an error other than ones listed below.

- MEDIA_NEEDED

```java
public static final
PrinterStateReason
MEDIA_NEEDED
```

A tray has run out of media.

- MEDIA_JAM

```java
public static final
PrinterStateReason
MEDIA_JAM
```

The device has a media jam.

- MOVING_TO_PAUSED

```java
public static final
PrinterStateReason
MOVING_TO_PAUSED
```

Someone has paused the printer, but the device(s) are taking an
appreciable time to stop. Later, when all output has stopped, the

PrinterState

becomes

STOPPED

, and the

PAUSED

value replaces the

MOVING_TO_PAUSED

value in the

PrinterStateReasons

attribute. This value
must be supported if the printer can be paused and the implementation
takes significant time to pause a device in certain circumstances.

- PAUSED

```java
public static final
PrinterStateReason
PAUSED
```

Someone has paused the printer and the printer's

PrinterState

is

STOPPED

. In this state, a
printer must not produce printed output, but it must perform other
operations requested by a client. If a printer had been printing a job
when the printer was paused, the

Printer

must resume printing
that job when the printer is no longer paused and leave no evidence in
the printed output of such a pause. This value must be supported if the
printer can be paused.

- SHUTDOWN

```java
public static final
PrinterStateReason
SHUTDOWN
```

Someone has removed a printer from service, and the device may be powered
down or physically removed. In this state, a printer must not produce
printed output, and unless the printer is realized by a print server that
is still active, the printer must perform no other operations requested
by a client. If a printer had been printing a job when it was shut down,
the printer need not resume printing that job when the printer is no
longer shut down. If the printer resumes printing such a job, it may
leave evidence in the printed output of such a shutdown, e.g. the part
printed before the shutdown may be printed a second time after the
shutdown.

- CONNECTING_TO_DEVICE

```java
public static final
PrinterStateReason
CONNECTING_TO_DEVICE
```

The printer has scheduled a job on the output device and is in the
process of connecting to a shared network output device (and might not be
able to actually start printing the job for an arbitrarily long time
depending on the usage of the output device by other servers on the
network).

- TIMED_OUT

```java
public static final
PrinterStateReason
TIMED_OUT
```

The server was able to connect to the output device (or is always
connected), but was unable to get a response from the output device.

- STOPPING

```java
public static final
PrinterStateReason
STOPPING
```

The printer is in the process of stopping the device and will be stopped
in a while. When the device is stopped, the printer will change the

PrinterState

to

STOPPED

. The

STOPPING

reason is never an error, even for a printer with a
single output device. When an output device ceases accepting jobs, the
printer's

PrinterStateReasons

will have this
reason while the output device completes printing.

- STOPPED_PARTLY

```java
public static final
PrinterStateReason
STOPPED_PARTLY
```

When a printer controls more than one output device, this reason
indicates that one or more output devices are stopped. If the reason's
severity is a report, fewer than half of the output devices are stopped.
If the reason's severity is a warning, half or more but fewer than all of
the output devices are stopped.

- TONER_LOW

```java
public static final
PrinterStateReason
TONER_LOW
```

The device is low on toner.

- TONER_EMPTY

```java
public static final
PrinterStateReason
TONER_EMPTY
```

The device is out of toner.

- SPOOL_AREA_FULL

```java
public static final
PrinterStateReason
SPOOL_AREA_FULL
```

The limit of persistent storage allocated for spooling has been reached.
The printer is temporarily unable to accept more jobs. The printer will
remove this reason when it is able to accept more jobs. This value should
be used by a non-spooling printer that only accepts one or a small number
jobs at a time or a spooling printer that has filled the spool space.

- COVER_OPEN

```java
public static final
PrinterStateReason
COVER_OPEN
```

One or more covers on the device are open.

- INTERLOCK_OPEN

```java
public static final
PrinterStateReason
INTERLOCK_OPEN
```

One or more interlock devices on the printer are unlocked.

- DOOR_OPEN

```java
public static final
PrinterStateReason
DOOR_OPEN
```

One or more doors on the device are open.

- INPUT_TRAY_MISSING

```java
public static final
PrinterStateReason
INPUT_TRAY_MISSING
```

One or more input trays are not in the device.

- MEDIA_LOW

```java
public static final
PrinterStateReason
MEDIA_LOW
```

At least one input tray is low on media.

- MEDIA_EMPTY

```java
public static final
PrinterStateReason
MEDIA_EMPTY
```

At least one input tray is empty.

- OUTPUT_TRAY_MISSING

```java
public static final
PrinterStateReason
OUTPUT_TRAY_MISSING
```

One or more output trays are not in the device.

- OUTPUT_AREA_ALMOST_FULL

```java
public static final
PrinterStateReason
OUTPUT_AREA_ALMOST_FULL
```

One or more output areas are almost full (e.g. tray, stacker, collator).

- OUTPUT_AREA_FULL

```java
public static final
PrinterStateReason
OUTPUT_AREA_FULL
```

One or more output areas are full (e.g. tray, stacker, collator).

- MARKER_SUPPLY_LOW

```java
public static final
PrinterStateReason
MARKER_SUPPLY_LOW
```

The device is low on at least one marker supply (e.g. toner, ink,
ribbon).

- MARKER_SUPPLY_EMPTY

```java
public static final
PrinterStateReason
MARKER_SUPPLY_EMPTY
```

The device is out of at least one marker supply (e.g. toner, ink,
ribbon).

- MARKER_WASTE_ALMOST_FULL

```java
public static final
PrinterStateReason
MARKER_WASTE_ALMOST_FULL
```

The device marker supply waste receptacle is almost full.

- MARKER_WASTE_FULL

```java
public static final
PrinterStateReason
MARKER_WASTE_FULL
```

The device marker supply waste receptacle is full.

- FUSER_OVER_TEMP

```java
public static final
PrinterStateReason
FUSER_OVER_TEMP
```

The fuser temperature is above normal.

- FUSER_UNDER_TEMP

```java
public static final
PrinterStateReason
FUSER_UNDER_TEMP
```

The fuser temperature is below normal.

- OPC_NEAR_EOL

```java
public static final
PrinterStateReason
OPC_NEAR_EOL
```

The optical photo conductor is near end of life.

- OPC_LIFE_OVER

```java
public static final
PrinterStateReason
OPC_LIFE_OVER
```

The optical photo conductor is no longer functioning.

- DEVELOPER_LOW

```java
public static final
PrinterStateReason
DEVELOPER_LOW
```

The device is low on developer.

- DEVELOPER_EMPTY

```java
public static final
PrinterStateReason
DEVELOPER_EMPTY
```

The device is out of developer.

- INTERPRETER_RESOURCE_UNAVAILABLE

```java
public static final
PrinterStateReason
INTERPRETER_RESOURCE_UNAVAILABLE
```

An interpreter resource is unavailable (e.g., font, form).

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PrinterStateReason

```java
protected PrinterStateReason​(int value)
```

Construct a new printer state reason enumeration value with the given
integer value.

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

PrinterStateReason

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

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category is class

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category name is

"printer-state-reason"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- OTHER

```java
public static final
PrinterStateReason
OTHER
```

The printer has detected an error other than ones listed below.

- MEDIA_NEEDED

```java
public static final
PrinterStateReason
MEDIA_NEEDED
```

A tray has run out of media.

- MEDIA_JAM

```java
public static final
PrinterStateReason
MEDIA_JAM
```

The device has a media jam.

- MOVING_TO_PAUSED

```java
public static final
PrinterStateReason
MOVING_TO_PAUSED
```

Someone has paused the printer, but the device(s) are taking an
appreciable time to stop. Later, when all output has stopped, the

PrinterState

becomes

STOPPED

, and the

PAUSED

value replaces the

MOVING_TO_PAUSED

value in the

PrinterStateReasons

attribute. This value
must be supported if the printer can be paused and the implementation
takes significant time to pause a device in certain circumstances.

- PAUSED

```java
public static final
PrinterStateReason
PAUSED
```

Someone has paused the printer and the printer's

PrinterState

is

STOPPED

. In this state, a
printer must not produce printed output, but it must perform other
operations requested by a client. If a printer had been printing a job
when the printer was paused, the

Printer

must resume printing
that job when the printer is no longer paused and leave no evidence in
the printed output of such a pause. This value must be supported if the
printer can be paused.

- SHUTDOWN

```java
public static final
PrinterStateReason
SHUTDOWN
```

Someone has removed a printer from service, and the device may be powered
down or physically removed. In this state, a printer must not produce
printed output, and unless the printer is realized by a print server that
is still active, the printer must perform no other operations requested
by a client. If a printer had been printing a job when it was shut down,
the printer need not resume printing that job when the printer is no
longer shut down. If the printer resumes printing such a job, it may
leave evidence in the printed output of such a shutdown, e.g. the part
printed before the shutdown may be printed a second time after the
shutdown.

- CONNECTING_TO_DEVICE

```java
public static final
PrinterStateReason
CONNECTING_TO_DEVICE
```

The printer has scheduled a job on the output device and is in the
process of connecting to a shared network output device (and might not be
able to actually start printing the job for an arbitrarily long time
depending on the usage of the output device by other servers on the
network).

- TIMED_OUT

```java
public static final
PrinterStateReason
TIMED_OUT
```

The server was able to connect to the output device (or is always
connected), but was unable to get a response from the output device.

- STOPPING

```java
public static final
PrinterStateReason
STOPPING
```

The printer is in the process of stopping the device and will be stopped
in a while. When the device is stopped, the printer will change the

PrinterState

to

STOPPED

. The

STOPPING

reason is never an error, even for a printer with a
single output device. When an output device ceases accepting jobs, the
printer's

PrinterStateReasons

will have this
reason while the output device completes printing.

- STOPPED_PARTLY

```java
public static final
PrinterStateReason
STOPPED_PARTLY
```

When a printer controls more than one output device, this reason
indicates that one or more output devices are stopped. If the reason's
severity is a report, fewer than half of the output devices are stopped.
If the reason's severity is a warning, half or more but fewer than all of
the output devices are stopped.

- TONER_LOW

```java
public static final
PrinterStateReason
TONER_LOW
```

The device is low on toner.

- TONER_EMPTY

```java
public static final
PrinterStateReason
TONER_EMPTY
```

The device is out of toner.

- SPOOL_AREA_FULL

```java
public static final
PrinterStateReason
SPOOL_AREA_FULL
```

The limit of persistent storage allocated for spooling has been reached.
The printer is temporarily unable to accept more jobs. The printer will
remove this reason when it is able to accept more jobs. This value should
be used by a non-spooling printer that only accepts one or a small number
jobs at a time or a spooling printer that has filled the spool space.

- COVER_OPEN

```java
public static final
PrinterStateReason
COVER_OPEN
```

One or more covers on the device are open.

- INTERLOCK_OPEN

```java
public static final
PrinterStateReason
INTERLOCK_OPEN
```

One or more interlock devices on the printer are unlocked.

- DOOR_OPEN

```java
public static final
PrinterStateReason
DOOR_OPEN
```

One or more doors on the device are open.

- INPUT_TRAY_MISSING

```java
public static final
PrinterStateReason
INPUT_TRAY_MISSING
```

One or more input trays are not in the device.

- MEDIA_LOW

```java
public static final
PrinterStateReason
MEDIA_LOW
```

At least one input tray is low on media.

- MEDIA_EMPTY

```java
public static final
PrinterStateReason
MEDIA_EMPTY
```

At least one input tray is empty.

- OUTPUT_TRAY_MISSING

```java
public static final
PrinterStateReason
OUTPUT_TRAY_MISSING
```

One or more output trays are not in the device.

- OUTPUT_AREA_ALMOST_FULL

```java
public static final
PrinterStateReason
OUTPUT_AREA_ALMOST_FULL
```

One or more output areas are almost full (e.g. tray, stacker, collator).

- OUTPUT_AREA_FULL

```java
public static final
PrinterStateReason
OUTPUT_AREA_FULL
```

One or more output areas are full (e.g. tray, stacker, collator).

- MARKER_SUPPLY_LOW

```java
public static final
PrinterStateReason
MARKER_SUPPLY_LOW
```

The device is low on at least one marker supply (e.g. toner, ink,
ribbon).

- MARKER_SUPPLY_EMPTY

```java
public static final
PrinterStateReason
MARKER_SUPPLY_EMPTY
```

The device is out of at least one marker supply (e.g. toner, ink,
ribbon).

- MARKER_WASTE_ALMOST_FULL

```java
public static final
PrinterStateReason
MARKER_WASTE_ALMOST_FULL
```

The device marker supply waste receptacle is almost full.

- MARKER_WASTE_FULL

```java
public static final
PrinterStateReason
MARKER_WASTE_FULL
```

The device marker supply waste receptacle is full.

- FUSER_OVER_TEMP

```java
public static final
PrinterStateReason
FUSER_OVER_TEMP
```

The fuser temperature is above normal.

- FUSER_UNDER_TEMP

```java
public static final
PrinterStateReason
FUSER_UNDER_TEMP
```

The fuser temperature is below normal.

- OPC_NEAR_EOL

```java
public static final
PrinterStateReason
OPC_NEAR_EOL
```

The optical photo conductor is near end of life.

- OPC_LIFE_OVER

```java
public static final
PrinterStateReason
OPC_LIFE_OVER
```

The optical photo conductor is no longer functioning.

- DEVELOPER_LOW

```java
public static final
PrinterStateReason
DEVELOPER_LOW
```

The device is low on developer.

- DEVELOPER_EMPTY

```java
public static final
PrinterStateReason
DEVELOPER_EMPTY
```

The device is out of developer.

- INTERPRETER_RESOURCE_UNAVAILABLE

```java
public static final
PrinterStateReason
INTERPRETER_RESOURCE_UNAVAILABLE
```

An interpreter resource is unavailable (e.g., font, form).

---

#### Field Detail

OTHER

```java
public static final
PrinterStateReason
OTHER
```

The printer has detected an error other than ones listed below.

---

#### OTHER

public static final

PrinterStateReason

OTHER

The printer has detected an error other than ones listed below.

MEDIA_NEEDED

```java
public static final
PrinterStateReason
MEDIA_NEEDED
```

A tray has run out of media.

---

#### MEDIA_NEEDED

public static final

PrinterStateReason

MEDIA_NEEDED

A tray has run out of media.

MEDIA_JAM

```java
public static final
PrinterStateReason
MEDIA_JAM
```

The device has a media jam.

---

#### MEDIA_JAM

public static final

PrinterStateReason

MEDIA_JAM

The device has a media jam.

MOVING_TO_PAUSED

```java
public static final
PrinterStateReason
MOVING_TO_PAUSED
```

Someone has paused the printer, but the device(s) are taking an
appreciable time to stop. Later, when all output has stopped, the

PrinterState

becomes

STOPPED

, and the

PAUSED

value replaces the

MOVING_TO_PAUSED

value in the

PrinterStateReasons

attribute. This value
must be supported if the printer can be paused and the implementation
takes significant time to pause a device in certain circumstances.

---

#### MOVING_TO_PAUSED

public static final

PrinterStateReason

MOVING_TO_PAUSED

Someone has paused the printer, but the device(s) are taking an
appreciable time to stop. Later, when all output has stopped, the

PrinterState

becomes

STOPPED

, and the

PAUSED

value replaces the

MOVING_TO_PAUSED

value in the

PrinterStateReasons

attribute. This value
must be supported if the printer can be paused and the implementation
takes significant time to pause a device in certain circumstances.

PAUSED

```java
public static final
PrinterStateReason
PAUSED
```

Someone has paused the printer and the printer's

PrinterState

is

STOPPED

. In this state, a
printer must not produce printed output, but it must perform other
operations requested by a client. If a printer had been printing a job
when the printer was paused, the

Printer

must resume printing
that job when the printer is no longer paused and leave no evidence in
the printed output of such a pause. This value must be supported if the
printer can be paused.

---

#### PAUSED

public static final

PrinterStateReason

PAUSED

Someone has paused the printer and the printer's

PrinterState

is

STOPPED

. In this state, a
printer must not produce printed output, but it must perform other
operations requested by a client. If a printer had been printing a job
when the printer was paused, the

Printer

must resume printing
that job when the printer is no longer paused and leave no evidence in
the printed output of such a pause. This value must be supported if the
printer can be paused.

SHUTDOWN

```java
public static final
PrinterStateReason
SHUTDOWN
```

Someone has removed a printer from service, and the device may be powered
down or physically removed. In this state, a printer must not produce
printed output, and unless the printer is realized by a print server that
is still active, the printer must perform no other operations requested
by a client. If a printer had been printing a job when it was shut down,
the printer need not resume printing that job when the printer is no
longer shut down. If the printer resumes printing such a job, it may
leave evidence in the printed output of such a shutdown, e.g. the part
printed before the shutdown may be printed a second time after the
shutdown.

---

#### SHUTDOWN

public static final

PrinterStateReason

SHUTDOWN

Someone has removed a printer from service, and the device may be powered
down or physically removed. In this state, a printer must not produce
printed output, and unless the printer is realized by a print server that
is still active, the printer must perform no other operations requested
by a client. If a printer had been printing a job when it was shut down,
the printer need not resume printing that job when the printer is no
longer shut down. If the printer resumes printing such a job, it may
leave evidence in the printed output of such a shutdown, e.g. the part
printed before the shutdown may be printed a second time after the
shutdown.

CONNECTING_TO_DEVICE

```java
public static final
PrinterStateReason
CONNECTING_TO_DEVICE
```

The printer has scheduled a job on the output device and is in the
process of connecting to a shared network output device (and might not be
able to actually start printing the job for an arbitrarily long time
depending on the usage of the output device by other servers on the
network).

---

#### CONNECTING_TO_DEVICE

public static final

PrinterStateReason

CONNECTING_TO_DEVICE

The printer has scheduled a job on the output device and is in the
process of connecting to a shared network output device (and might not be
able to actually start printing the job for an arbitrarily long time
depending on the usage of the output device by other servers on the
network).

TIMED_OUT

```java
public static final
PrinterStateReason
TIMED_OUT
```

The server was able to connect to the output device (or is always
connected), but was unable to get a response from the output device.

---

#### TIMED_OUT

public static final

PrinterStateReason

TIMED_OUT

The server was able to connect to the output device (or is always
connected), but was unable to get a response from the output device.

STOPPING

```java
public static final
PrinterStateReason
STOPPING
```

The printer is in the process of stopping the device and will be stopped
in a while. When the device is stopped, the printer will change the

PrinterState

to

STOPPED

. The

STOPPING

reason is never an error, even for a printer with a
single output device. When an output device ceases accepting jobs, the
printer's

PrinterStateReasons

will have this
reason while the output device completes printing.

---

#### STOPPING

public static final

PrinterStateReason

STOPPING

The printer is in the process of stopping the device and will be stopped
in a while. When the device is stopped, the printer will change the

PrinterState

to

STOPPED

. The

STOPPING

reason is never an error, even for a printer with a
single output device. When an output device ceases accepting jobs, the
printer's

PrinterStateReasons

will have this
reason while the output device completes printing.

STOPPED_PARTLY

```java
public static final
PrinterStateReason
STOPPED_PARTLY
```

When a printer controls more than one output device, this reason
indicates that one or more output devices are stopped. If the reason's
severity is a report, fewer than half of the output devices are stopped.
If the reason's severity is a warning, half or more but fewer than all of
the output devices are stopped.

---

#### STOPPED_PARTLY

public static final

PrinterStateReason

STOPPED_PARTLY

When a printer controls more than one output device, this reason
indicates that one or more output devices are stopped. If the reason's
severity is a report, fewer than half of the output devices are stopped.
If the reason's severity is a warning, half or more but fewer than all of
the output devices are stopped.

TONER_LOW

```java
public static final
PrinterStateReason
TONER_LOW
```

The device is low on toner.

---

#### TONER_LOW

public static final

PrinterStateReason

TONER_LOW

The device is low on toner.

TONER_EMPTY

```java
public static final
PrinterStateReason
TONER_EMPTY
```

The device is out of toner.

---

#### TONER_EMPTY

public static final

PrinterStateReason

TONER_EMPTY

The device is out of toner.

SPOOL_AREA_FULL

```java
public static final
PrinterStateReason
SPOOL_AREA_FULL
```

The limit of persistent storage allocated for spooling has been reached.
The printer is temporarily unable to accept more jobs. The printer will
remove this reason when it is able to accept more jobs. This value should
be used by a non-spooling printer that only accepts one or a small number
jobs at a time or a spooling printer that has filled the spool space.

---

#### SPOOL_AREA_FULL

public static final

PrinterStateReason

SPOOL_AREA_FULL

The limit of persistent storage allocated for spooling has been reached.
The printer is temporarily unable to accept more jobs. The printer will
remove this reason when it is able to accept more jobs. This value should
be used by a non-spooling printer that only accepts one or a small number
jobs at a time or a spooling printer that has filled the spool space.

COVER_OPEN

```java
public static final
PrinterStateReason
COVER_OPEN
```

One or more covers on the device are open.

---

#### COVER_OPEN

public static final

PrinterStateReason

COVER_OPEN

One or more covers on the device are open.

INTERLOCK_OPEN

```java
public static final
PrinterStateReason
INTERLOCK_OPEN
```

One or more interlock devices on the printer are unlocked.

---

#### INTERLOCK_OPEN

public static final

PrinterStateReason

INTERLOCK_OPEN

One or more interlock devices on the printer are unlocked.

DOOR_OPEN

```java
public static final
PrinterStateReason
DOOR_OPEN
```

One or more doors on the device are open.

---

#### DOOR_OPEN

public static final

PrinterStateReason

DOOR_OPEN

One or more doors on the device are open.

INPUT_TRAY_MISSING

```java
public static final
PrinterStateReason
INPUT_TRAY_MISSING
```

One or more input trays are not in the device.

---

#### INPUT_TRAY_MISSING

public static final

PrinterStateReason

INPUT_TRAY_MISSING

One or more input trays are not in the device.

MEDIA_LOW

```java
public static final
PrinterStateReason
MEDIA_LOW
```

At least one input tray is low on media.

---

#### MEDIA_LOW

public static final

PrinterStateReason

MEDIA_LOW

At least one input tray is low on media.

MEDIA_EMPTY

```java
public static final
PrinterStateReason
MEDIA_EMPTY
```

At least one input tray is empty.

---

#### MEDIA_EMPTY

public static final

PrinterStateReason

MEDIA_EMPTY

At least one input tray is empty.

OUTPUT_TRAY_MISSING

```java
public static final
PrinterStateReason
OUTPUT_TRAY_MISSING
```

One or more output trays are not in the device.

---

#### OUTPUT_TRAY_MISSING

public static final

PrinterStateReason

OUTPUT_TRAY_MISSING

One or more output trays are not in the device.

OUTPUT_AREA_ALMOST_FULL

```java
public static final
PrinterStateReason
OUTPUT_AREA_ALMOST_FULL
```

One or more output areas are almost full (e.g. tray, stacker, collator).

---

#### OUTPUT_AREA_ALMOST_FULL

public static final

PrinterStateReason

OUTPUT_AREA_ALMOST_FULL

One or more output areas are almost full (e.g. tray, stacker, collator).

OUTPUT_AREA_FULL

```java
public static final
PrinterStateReason
OUTPUT_AREA_FULL
```

One or more output areas are full (e.g. tray, stacker, collator).

---

#### OUTPUT_AREA_FULL

public static final

PrinterStateReason

OUTPUT_AREA_FULL

One or more output areas are full (e.g. tray, stacker, collator).

MARKER_SUPPLY_LOW

```java
public static final
PrinterStateReason
MARKER_SUPPLY_LOW
```

The device is low on at least one marker supply (e.g. toner, ink,
ribbon).

---

#### MARKER_SUPPLY_LOW

public static final

PrinterStateReason

MARKER_SUPPLY_LOW

The device is low on at least one marker supply (e.g. toner, ink,
ribbon).

MARKER_SUPPLY_EMPTY

```java
public static final
PrinterStateReason
MARKER_SUPPLY_EMPTY
```

The device is out of at least one marker supply (e.g. toner, ink,
ribbon).

---

#### MARKER_SUPPLY_EMPTY

public static final

PrinterStateReason

MARKER_SUPPLY_EMPTY

The device is out of at least one marker supply (e.g. toner, ink,
ribbon).

MARKER_WASTE_ALMOST_FULL

```java
public static final
PrinterStateReason
MARKER_WASTE_ALMOST_FULL
```

The device marker supply waste receptacle is almost full.

---

#### MARKER_WASTE_ALMOST_FULL

public static final

PrinterStateReason

MARKER_WASTE_ALMOST_FULL

The device marker supply waste receptacle is almost full.

MARKER_WASTE_FULL

```java
public static final
PrinterStateReason
MARKER_WASTE_FULL
```

The device marker supply waste receptacle is full.

---

#### MARKER_WASTE_FULL

public static final

PrinterStateReason

MARKER_WASTE_FULL

The device marker supply waste receptacle is full.

FUSER_OVER_TEMP

```java
public static final
PrinterStateReason
FUSER_OVER_TEMP
```

The fuser temperature is above normal.

---

#### FUSER_OVER_TEMP

public static final

PrinterStateReason

FUSER_OVER_TEMP

The fuser temperature is above normal.

FUSER_UNDER_TEMP

```java
public static final
PrinterStateReason
FUSER_UNDER_TEMP
```

The fuser temperature is below normal.

---

#### FUSER_UNDER_TEMP

public static final

PrinterStateReason

FUSER_UNDER_TEMP

The fuser temperature is below normal.

OPC_NEAR_EOL

```java
public static final
PrinterStateReason
OPC_NEAR_EOL
```

The optical photo conductor is near end of life.

---

#### OPC_NEAR_EOL

public static final

PrinterStateReason

OPC_NEAR_EOL

The optical photo conductor is near end of life.

OPC_LIFE_OVER

```java
public static final
PrinterStateReason
OPC_LIFE_OVER
```

The optical photo conductor is no longer functioning.

---

#### OPC_LIFE_OVER

public static final

PrinterStateReason

OPC_LIFE_OVER

The optical photo conductor is no longer functioning.

DEVELOPER_LOW

```java
public static final
PrinterStateReason
DEVELOPER_LOW
```

The device is low on developer.

---

#### DEVELOPER_LOW

public static final

PrinterStateReason

DEVELOPER_LOW

The device is low on developer.

DEVELOPER_EMPTY

```java
public static final
PrinterStateReason
DEVELOPER_EMPTY
```

The device is out of developer.

---

#### DEVELOPER_EMPTY

public static final

PrinterStateReason

DEVELOPER_EMPTY

The device is out of developer.

INTERPRETER_RESOURCE_UNAVAILABLE

```java
public static final
PrinterStateReason
INTERPRETER_RESOURCE_UNAVAILABLE
```

An interpreter resource is unavailable (e.g., font, form).

---

#### INTERPRETER_RESOURCE_UNAVAILABLE

public static final

PrinterStateReason

INTERPRETER_RESOURCE_UNAVAILABLE

An interpreter resource is unavailable (e.g., font, form).

Constructor Detail

- PrinterStateReason

```java
protected PrinterStateReason​(int value)
```

Construct a new printer state reason enumeration value with the given
integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

PrinterStateReason

```java
protected PrinterStateReason​(int value)
```

Construct a new printer state reason enumeration value with the given
integer value.

**Parameters:** value

- Integer value

---

#### PrinterStateReason

protected PrinterStateReason​(int value)

Construct a new printer state reason enumeration value with the given
integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

PrinterStateReason

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

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category is class

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category name is

"printer-state-reason"

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

PrinterStateReason

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

PrinterStateReason

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

PrinterStateReason

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

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category is class

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category is class

PrinterStateReason

itself.

For class

PrinterStateReason

and any vendor-defined subclasses,
the category is class

PrinterStateReason

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

PrinterStateReason

and any vendor-defined subclasses,
the category name is

"printer-state-reason"

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

PrinterStateReason

and any vendor-defined subclasses,
the category name is

"printer-state-reason"

.

For class

PrinterStateReason

and any vendor-defined subclasses,
the category name is

"printer-state-reason"

.

---


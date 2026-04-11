# Class ProgressMonitor

**Source:** `java.desktop\javax\swing\ProgressMonitor.html`

### Class Description

```java
public class
ProgressMonitor

extends
Object

implements
Accessible
```

A class to monitor the progress of some operation. If it looks
like the operation will take a while, a progress dialog will be popped up.
When the ProgressMonitor is created it is given a numeric range and a
descriptive string. As the operation progresses, call the setProgress method
to indicate how far along the [min,max] range the operation is.
Initially, there is no ProgressDialog. After the first millisToDecideToPopup
milliseconds (default 500) the progress monitor will predict how long
the operation will take. If it is longer than millisToPopup (default 2000,
2 seconds) a ProgressDialog will be popped up.

From time to time, when the Dialog box is visible, the progress bar will
be updated when setProgress is called. setProgress won't always update
the progress bar, it will only be done if the amount of progress is
visibly significant.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

**All Implemented Interfaces:** Accessible

---

### Field Details

#### protected
AccessibleContext
accessibleContext

The

AccessibleContext

for the

ProgressMonitor

**Since:**
- 1.5

---

### Constructor Details

#### public ProgressMonitor​(
Component
parentComponent,

Object
message,

String
note,
int min,
int max)

Constructs a graphic object that shows progress, typically by filling
in a rectangular bar as the process nears completion.

**Parameters:**
- parentComponent

- the parent component for the dialog box
- message

- a descriptive message that will be shown
to the user to indicate what operation is being monitored.
This does not change as the operation progresses.
See the message parameters to methods in

JOptionPane.message

for the range of values.
- note

- a short note describing the state of the
operation. As the operation progresses, you can call
setNote to change the note displayed. This is used,
for example, in operations that iterate through a
list of files to show the name of the file being processes.
If note is initially null, there will be no note line
in the dialog box and setNote will be ineffective
- min

- the lower bound of the range
- max

- the upper bound of the range

**See Also:**
- JDialog

,

JOptionPane

---

### Method Details

#### public void setProgress​(int nv)

Indicate the progress of the operation being monitored.
If the specified value is >= the maximum, the progress
monitor is closed.

**Parameters:**
- nv

- an int specifying the current value, between the
maximum and minimum specified for this component

**See Also:**
- setMinimum(int)

,

setMaximum(int)

,

close()

---

#### public void close()

Indicate that the operation is complete. This happens automatically
when the value set by setProgress is >= max, but it may be called
earlier if the operation ends early.

---

#### public int getMinimum()

Returns the minimum value -- the lower end of the progress value.

**Returns:**
- an int representing the minimum value

**See Also:**
- setMinimum(int)

---

#### public void setMinimum​(int m)

Specifies the minimum value.

**Parameters:**
- m

- an int specifying the minimum value

**See Also:**
- getMinimum()

---

#### public int getMaximum()

Returns the maximum value -- the higher end of the progress value.

**Returns:**
- an int representing the maximum value

**See Also:**
- setMaximum(int)

---

#### public void setMaximum​(int m)

Specifies the maximum value.

**Parameters:**
- m

- an int specifying the maximum value

**See Also:**
- getMaximum()

---

#### public boolean isCanceled()

Returns true if the user hits the Cancel button or closes
the progress dialog.

**Returns:**
- true if the user hits the Cancel button or closes
the progress dialog

---

#### public void setMillisToDecideToPopup​(int millisToDecideToPopup)

Specifies the amount of time to wait before deciding whether or
not to popup a progress monitor.

**Parameters:**
- millisToDecideToPopup

- an int specifying the time to wait,
in milliseconds

**See Also:**
- getMillisToDecideToPopup()

---

#### public int getMillisToDecideToPopup()

Returns the amount of time this object waits before deciding whether
or not to popup a progress monitor.

**Returns:**
- the amount of time in milliseconds this object waits before
deciding whether or not to popup a progress monitor

**See Also:**
- setMillisToDecideToPopup(int)

---

#### public void setMillisToPopup​(int millisToPopup)

Specifies the amount of time it will take for the popup to appear.
(If the predicted time remaining is less than this time, the popup
won't be displayed.)

**Parameters:**
- millisToPopup

- an int specifying the time in milliseconds

**See Also:**
- getMillisToPopup()

---

#### public int getMillisToPopup()

Returns the amount of time it will take for the popup to appear.

**Returns:**
- the amont of time in milliseconds it will take for the
popup to appear

**See Also:**
- setMillisToPopup(int)

---

#### public void setNote​(
String
note)

Specifies the additional note that is displayed along with the
progress message. Used, for example, to show which file the
is currently being copied during a multiple-file copy.

**Parameters:**
- note

- a String specifying the note to display

**See Also:**
- getNote()

---

#### public
String
getNote()

Specifies the additional note that is displayed along with the
progress message.

**Returns:**
- a String specifying the note to display

**See Also:**
- setNote(java.lang.String)

---

#### public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

for the

ProgressMonitor

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Returns:**
- the

AccessibleContext

for the

ProgressMonitor

**Since:**
- 1.5

---

### Additional Sections

#### Class ProgressMonitor

java.lang.Object

- javax.swing.ProgressMonitor

javax.swing.ProgressMonitor

**All Implemented Interfaces:** Accessible

```java
public class
ProgressMonitor

extends
Object

implements
Accessible
```

A class to monitor the progress of some operation. If it looks
like the operation will take a while, a progress dialog will be popped up.
When the ProgressMonitor is created it is given a numeric range and a
descriptive string. As the operation progresses, call the setProgress method
to indicate how far along the [min,max] range the operation is.
Initially, there is no ProgressDialog. After the first millisToDecideToPopup
milliseconds (default 500) the progress monitor will predict how long
the operation will take. If it is longer than millisToPopup (default 2000,
2 seconds) a ProgressDialog will be popped up.

From time to time, when the Dialog box is visible, the progress bar will
be updated when setProgress is called. setProgress won't always update
the progress bar, it will only be done if the amount of progress is
visibly significant.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

**Since:** 1.2
**See Also:** ProgressMonitorInputStream

public class

ProgressMonitor

extends

Object

implements

Accessible

A class to monitor the progress of some operation. If it looks
like the operation will take a while, a progress dialog will be popped up.
When the ProgressMonitor is created it is given a numeric range and a
descriptive string. As the operation progresses, call the setProgress method
to indicate how far along the [min,max] range the operation is.
Initially, there is no ProgressDialog. After the first millisToDecideToPopup
milliseconds (default 500) the progress monitor will predict how long
the operation will take. If it is longer than millisToPopup (default 2000,
2 seconds) a ProgressDialog will be popped up.

From time to time, when the Dialog box is visible, the progress bar will
be updated when setProgress is called. setProgress won't always update
the progress bar, it will only be done if the amount of progress is
visibly significant.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

From time to time, when the Dialog box is visible, the progress bar will
be updated when setProgress is called. setProgress won't always update
the progress bar, it will only be done if the amount of progress is
visibly significant.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

ProgressMonitor.AccessibleProgressMonitor

AccessibleProgressMonitor

implements accessibility
support for the

ProgressMonitor

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

AccessibleContext

accessibleContext

The

AccessibleContext

for the

ProgressMonitor

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ProgressMonitor

​(

Component

parentComponent,

Object

message,

String

note,
int min,
int max)

Constructs a graphic object that shows progress, typically by filling
in a rectangular bar as the process nears completion.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Indicate that the operation is complete.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

for the

ProgressMonitor

int

getMaximum

()

Returns the maximum value -- the higher end of the progress value.

int

getMillisToDecideToPopup

()

Returns the amount of time this object waits before deciding whether
or not to popup a progress monitor.

int

getMillisToPopup

()

Returns the amount of time it will take for the popup to appear.

int

getMinimum

()

Returns the minimum value -- the lower end of the progress value.

String

getNote

()

Specifies the additional note that is displayed along with the
progress message.

boolean

isCanceled

()

Returns true if the user hits the Cancel button or closes
the progress dialog.

void

setMaximum

​(int m)

Specifies the maximum value.

void

setMillisToDecideToPopup

​(int millisToDecideToPopup)

Specifies the amount of time to wait before deciding whether or
not to popup a progress monitor.

void

setMillisToPopup

​(int millisToPopup)

Specifies the amount of time it will take for the popup to appear.

void

setMinimum

​(int m)

Specifies the minimum value.

void

setNote

​(

String

note)

Specifies the additional note that is displayed along with the
progress message.

void

setProgress

​(int nv)

Indicate the progress of the operation being monitored.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

ProgressMonitor.AccessibleProgressMonitor

AccessibleProgressMonitor

implements accessibility
support for the

ProgressMonitor

class.

---

#### Nested Class Summary

AccessibleProgressMonitor

implements accessibility
support for the

ProgressMonitor

class.

Field Summary

Fields

Modifier and Type

Field

Description

protected

AccessibleContext

accessibleContext

The

AccessibleContext

for the

ProgressMonitor

---

#### Field Summary

The

AccessibleContext

for the

ProgressMonitor

Constructor Summary

Constructors

Constructor

Description

ProgressMonitor

​(

Component

parentComponent,

Object

message,

String

note,
int min,
int max)

Constructs a graphic object that shows progress, typically by filling
in a rectangular bar as the process nears completion.

---

#### Constructor Summary

Constructs a graphic object that shows progress, typically by filling
in a rectangular bar as the process nears completion.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Indicate that the operation is complete.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

for the

ProgressMonitor

int

getMaximum

()

Returns the maximum value -- the higher end of the progress value.

int

getMillisToDecideToPopup

()

Returns the amount of time this object waits before deciding whether
or not to popup a progress monitor.

int

getMillisToPopup

()

Returns the amount of time it will take for the popup to appear.

int

getMinimum

()

Returns the minimum value -- the lower end of the progress value.

String

getNote

()

Specifies the additional note that is displayed along with the
progress message.

boolean

isCanceled

()

Returns true if the user hits the Cancel button or closes
the progress dialog.

void

setMaximum

​(int m)

Specifies the maximum value.

void

setMillisToDecideToPopup

​(int millisToDecideToPopup)

Specifies the amount of time to wait before deciding whether or
not to popup a progress monitor.

void

setMillisToPopup

​(int millisToPopup)

Specifies the amount of time it will take for the popup to appear.

void

setMinimum

​(int m)

Specifies the minimum value.

void

setNote

​(

String

note)

Specifies the additional note that is displayed along with the
progress message.

void

setProgress

​(int nv)

Indicate the progress of the operation being monitored.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Indicate that the operation is complete.

Gets the

AccessibleContext

for the

ProgressMonitor

Returns the maximum value -- the higher end of the progress value.

Returns the amount of time this object waits before deciding whether
or not to popup a progress monitor.

Returns the amount of time it will take for the popup to appear.

Returns the minimum value -- the lower end of the progress value.

Specifies the additional note that is displayed along with the
progress message.

Returns true if the user hits the Cancel button or closes
the progress dialog.

Specifies the maximum value.

Specifies the amount of time to wait before deciding whether or
not to popup a progress monitor.

Specifies the amount of time it will take for the popup to appear.

Specifies the minimum value.

Indicate the progress of the operation being monitored.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

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

- accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The

AccessibleContext

for the

ProgressMonitor

**Since:** 1.5

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ProgressMonitor

```java
public ProgressMonitor​(
Component
parentComponent,

Object
message,

String
note,
int min,
int max)
```

Constructs a graphic object that shows progress, typically by filling
in a rectangular bar as the process nears completion.

**Parameters:** parentComponent

- the parent component for the dialog box
**Parameters:** message

- a descriptive message that will be shown
to the user to indicate what operation is being monitored.
This does not change as the operation progresses.
See the message parameters to methods in

JOptionPane.message

for the range of values.
**Parameters:** note

- a short note describing the state of the
operation. As the operation progresses, you can call
setNote to change the note displayed. This is used,
for example, in operations that iterate through a
list of files to show the name of the file being processes.
If note is initially null, there will be no note line
in the dialog box and setNote will be ineffective
**Parameters:** min

- the lower bound of the range
**Parameters:** max

- the upper bound of the range
**See Also:** JDialog

,

JOptionPane

============ METHOD DETAIL ==========

- Method Detail

- setProgress

```java
public void setProgress​(int nv)
```

Indicate the progress of the operation being monitored.
If the specified value is >= the maximum, the progress
monitor is closed.

**Parameters:** nv

- an int specifying the current value, between the
maximum and minimum specified for this component
**See Also:** setMinimum(int)

,

setMaximum(int)

,

close()

- close

```java
public void close()
```

Indicate that the operation is complete. This happens automatically
when the value set by setProgress is >= max, but it may be called
earlier if the operation ends early.

- getMinimum

```java
public int getMinimum()
```

Returns the minimum value -- the lower end of the progress value.

**Returns:** an int representing the minimum value
**See Also:** setMinimum(int)

- setMinimum

```java
public void setMinimum​(int m)
```

Specifies the minimum value.

**Parameters:** m

- an int specifying the minimum value
**See Also:** getMinimum()

- getMaximum

```java
public int getMaximum()
```

Returns the maximum value -- the higher end of the progress value.

**Returns:** an int representing the maximum value
**See Also:** setMaximum(int)

- setMaximum

```java
public void setMaximum​(int m)
```

Specifies the maximum value.

**Parameters:** m

- an int specifying the maximum value
**See Also:** getMaximum()

- isCanceled

```java
public boolean isCanceled()
```

Returns true if the user hits the Cancel button or closes
the progress dialog.

**Returns:** true if the user hits the Cancel button or closes
the progress dialog

- setMillisToDecideToPopup

```java
public void setMillisToDecideToPopup​(int millisToDecideToPopup)
```

Specifies the amount of time to wait before deciding whether or
not to popup a progress monitor.

**Parameters:** millisToDecideToPopup

- an int specifying the time to wait,
in milliseconds
**See Also:** getMillisToDecideToPopup()

- getMillisToDecideToPopup

```java
public int getMillisToDecideToPopup()
```

Returns the amount of time this object waits before deciding whether
or not to popup a progress monitor.

**Returns:** the amount of time in milliseconds this object waits before
deciding whether or not to popup a progress monitor
**See Also:** setMillisToDecideToPopup(int)

- setMillisToPopup

```java
public void setMillisToPopup​(int millisToPopup)
```

Specifies the amount of time it will take for the popup to appear.
(If the predicted time remaining is less than this time, the popup
won't be displayed.)

**Parameters:** millisToPopup

- an int specifying the time in milliseconds
**See Also:** getMillisToPopup()

- getMillisToPopup

```java
public int getMillisToPopup()
```

Returns the amount of time it will take for the popup to appear.

**Returns:** the amont of time in milliseconds it will take for the
popup to appear
**See Also:** setMillisToPopup(int)

- setNote

```java
public void setNote​(
String
note)
```

Specifies the additional note that is displayed along with the
progress message. Used, for example, to show which file the
is currently being copied during a multiple-file copy.

**Parameters:** note

- a String specifying the note to display
**See Also:** getNote()

- getNote

```java
public
String
getNote()
```

Specifies the additional note that is displayed along with the
progress message.

**Returns:** a String specifying the note to display
**See Also:** setNote(java.lang.String)

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

for the

ProgressMonitor

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the

AccessibleContext

for the

ProgressMonitor
**Since:** 1.5

Field Detail

- accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The

AccessibleContext

for the

ProgressMonitor

**Since:** 1.5

---

#### Field Detail

accessibleContext

```java
protected
AccessibleContext
accessibleContext
```

The

AccessibleContext

for the

ProgressMonitor

**Since:** 1.5

---

#### accessibleContext

protected

AccessibleContext

accessibleContext

The

AccessibleContext

for the

ProgressMonitor

Constructor Detail

- ProgressMonitor

```java
public ProgressMonitor​(
Component
parentComponent,

Object
message,

String
note,
int min,
int max)
```

Constructs a graphic object that shows progress, typically by filling
in a rectangular bar as the process nears completion.

**Parameters:** parentComponent

- the parent component for the dialog box
**Parameters:** message

- a descriptive message that will be shown
to the user to indicate what operation is being monitored.
This does not change as the operation progresses.
See the message parameters to methods in

JOptionPane.message

for the range of values.
**Parameters:** note

- a short note describing the state of the
operation. As the operation progresses, you can call
setNote to change the note displayed. This is used,
for example, in operations that iterate through a
list of files to show the name of the file being processes.
If note is initially null, there will be no note line
in the dialog box and setNote will be ineffective
**Parameters:** min

- the lower bound of the range
**Parameters:** max

- the upper bound of the range
**See Also:** JDialog

,

JOptionPane

---

#### Constructor Detail

ProgressMonitor

```java
public ProgressMonitor​(
Component
parentComponent,

Object
message,

String
note,
int min,
int max)
```

Constructs a graphic object that shows progress, typically by filling
in a rectangular bar as the process nears completion.

**Parameters:** parentComponent

- the parent component for the dialog box
**Parameters:** message

- a descriptive message that will be shown
to the user to indicate what operation is being monitored.
This does not change as the operation progresses.
See the message parameters to methods in

JOptionPane.message

for the range of values.
**Parameters:** note

- a short note describing the state of the
operation. As the operation progresses, you can call
setNote to change the note displayed. This is used,
for example, in operations that iterate through a
list of files to show the name of the file being processes.
If note is initially null, there will be no note line
in the dialog box and setNote will be ineffective
**Parameters:** min

- the lower bound of the range
**Parameters:** max

- the upper bound of the range
**See Also:** JDialog

,

JOptionPane

---

#### ProgressMonitor

public ProgressMonitor​(

Component

parentComponent,

Object

message,

String

note,
int min,
int max)

Constructs a graphic object that shows progress, typically by filling
in a rectangular bar as the process nears completion.

Method Detail

- setProgress

```java
public void setProgress​(int nv)
```

Indicate the progress of the operation being monitored.
If the specified value is >= the maximum, the progress
monitor is closed.

**Parameters:** nv

- an int specifying the current value, between the
maximum and minimum specified for this component
**See Also:** setMinimum(int)

,

setMaximum(int)

,

close()

- close

```java
public void close()
```

Indicate that the operation is complete. This happens automatically
when the value set by setProgress is >= max, but it may be called
earlier if the operation ends early.

- getMinimum

```java
public int getMinimum()
```

Returns the minimum value -- the lower end of the progress value.

**Returns:** an int representing the minimum value
**See Also:** setMinimum(int)

- setMinimum

```java
public void setMinimum​(int m)
```

Specifies the minimum value.

**Parameters:** m

- an int specifying the minimum value
**See Also:** getMinimum()

- getMaximum

```java
public int getMaximum()
```

Returns the maximum value -- the higher end of the progress value.

**Returns:** an int representing the maximum value
**See Also:** setMaximum(int)

- setMaximum

```java
public void setMaximum​(int m)
```

Specifies the maximum value.

**Parameters:** m

- an int specifying the maximum value
**See Also:** getMaximum()

- isCanceled

```java
public boolean isCanceled()
```

Returns true if the user hits the Cancel button or closes
the progress dialog.

**Returns:** true if the user hits the Cancel button or closes
the progress dialog

- setMillisToDecideToPopup

```java
public void setMillisToDecideToPopup​(int millisToDecideToPopup)
```

Specifies the amount of time to wait before deciding whether or
not to popup a progress monitor.

**Parameters:** millisToDecideToPopup

- an int specifying the time to wait,
in milliseconds
**See Also:** getMillisToDecideToPopup()

- getMillisToDecideToPopup

```java
public int getMillisToDecideToPopup()
```

Returns the amount of time this object waits before deciding whether
or not to popup a progress monitor.

**Returns:** the amount of time in milliseconds this object waits before
deciding whether or not to popup a progress monitor
**See Also:** setMillisToDecideToPopup(int)

- setMillisToPopup

```java
public void setMillisToPopup​(int millisToPopup)
```

Specifies the amount of time it will take for the popup to appear.
(If the predicted time remaining is less than this time, the popup
won't be displayed.)

**Parameters:** millisToPopup

- an int specifying the time in milliseconds
**See Also:** getMillisToPopup()

- getMillisToPopup

```java
public int getMillisToPopup()
```

Returns the amount of time it will take for the popup to appear.

**Returns:** the amont of time in milliseconds it will take for the
popup to appear
**See Also:** setMillisToPopup(int)

- setNote

```java
public void setNote​(
String
note)
```

Specifies the additional note that is displayed along with the
progress message. Used, for example, to show which file the
is currently being copied during a multiple-file copy.

**Parameters:** note

- a String specifying the note to display
**See Also:** getNote()

- getNote

```java
public
String
getNote()
```

Specifies the additional note that is displayed along with the
progress message.

**Returns:** a String specifying the note to display
**See Also:** setNote(java.lang.String)

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

for the

ProgressMonitor

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the

AccessibleContext

for the

ProgressMonitor
**Since:** 1.5

---

#### Method Detail

setProgress

```java
public void setProgress​(int nv)
```

Indicate the progress of the operation being monitored.
If the specified value is >= the maximum, the progress
monitor is closed.

**Parameters:** nv

- an int specifying the current value, between the
maximum and minimum specified for this component
**See Also:** setMinimum(int)

,

setMaximum(int)

,

close()

---

#### setProgress

public void setProgress​(int nv)

Indicate the progress of the operation being monitored.
If the specified value is >= the maximum, the progress
monitor is closed.

close

```java
public void close()
```

Indicate that the operation is complete. This happens automatically
when the value set by setProgress is >= max, but it may be called
earlier if the operation ends early.

---

#### close

public void close()

Indicate that the operation is complete. This happens automatically
when the value set by setProgress is >= max, but it may be called
earlier if the operation ends early.

getMinimum

```java
public int getMinimum()
```

Returns the minimum value -- the lower end of the progress value.

**Returns:** an int representing the minimum value
**See Also:** setMinimum(int)

---

#### getMinimum

public int getMinimum()

Returns the minimum value -- the lower end of the progress value.

setMinimum

```java
public void setMinimum​(int m)
```

Specifies the minimum value.

**Parameters:** m

- an int specifying the minimum value
**See Also:** getMinimum()

---

#### setMinimum

public void setMinimum​(int m)

Specifies the minimum value.

getMaximum

```java
public int getMaximum()
```

Returns the maximum value -- the higher end of the progress value.

**Returns:** an int representing the maximum value
**See Also:** setMaximum(int)

---

#### getMaximum

public int getMaximum()

Returns the maximum value -- the higher end of the progress value.

setMaximum

```java
public void setMaximum​(int m)
```

Specifies the maximum value.

**Parameters:** m

- an int specifying the maximum value
**See Also:** getMaximum()

---

#### setMaximum

public void setMaximum​(int m)

Specifies the maximum value.

isCanceled

```java
public boolean isCanceled()
```

Returns true if the user hits the Cancel button or closes
the progress dialog.

**Returns:** true if the user hits the Cancel button or closes
the progress dialog

---

#### isCanceled

public boolean isCanceled()

Returns true if the user hits the Cancel button or closes
the progress dialog.

setMillisToDecideToPopup

```java
public void setMillisToDecideToPopup​(int millisToDecideToPopup)
```

Specifies the amount of time to wait before deciding whether or
not to popup a progress monitor.

**Parameters:** millisToDecideToPopup

- an int specifying the time to wait,
in milliseconds
**See Also:** getMillisToDecideToPopup()

---

#### setMillisToDecideToPopup

public void setMillisToDecideToPopup​(int millisToDecideToPopup)

Specifies the amount of time to wait before deciding whether or
not to popup a progress monitor.

getMillisToDecideToPopup

```java
public int getMillisToDecideToPopup()
```

Returns the amount of time this object waits before deciding whether
or not to popup a progress monitor.

**Returns:** the amount of time in milliseconds this object waits before
deciding whether or not to popup a progress monitor
**See Also:** setMillisToDecideToPopup(int)

---

#### getMillisToDecideToPopup

public int getMillisToDecideToPopup()

Returns the amount of time this object waits before deciding whether
or not to popup a progress monitor.

setMillisToPopup

```java
public void setMillisToPopup​(int millisToPopup)
```

Specifies the amount of time it will take for the popup to appear.
(If the predicted time remaining is less than this time, the popup
won't be displayed.)

**Parameters:** millisToPopup

- an int specifying the time in milliseconds
**See Also:** getMillisToPopup()

---

#### setMillisToPopup

public void setMillisToPopup​(int millisToPopup)

Specifies the amount of time it will take for the popup to appear.
(If the predicted time remaining is less than this time, the popup
won't be displayed.)

getMillisToPopup

```java
public int getMillisToPopup()
```

Returns the amount of time it will take for the popup to appear.

**Returns:** the amont of time in milliseconds it will take for the
popup to appear
**See Also:** setMillisToPopup(int)

---

#### getMillisToPopup

public int getMillisToPopup()

Returns the amount of time it will take for the popup to appear.

setNote

```java
public void setNote​(
String
note)
```

Specifies the additional note that is displayed along with the
progress message. Used, for example, to show which file the
is currently being copied during a multiple-file copy.

**Parameters:** note

- a String specifying the note to display
**See Also:** getNote()

---

#### setNote

public void setNote​(

String

note)

Specifies the additional note that is displayed along with the
progress message. Used, for example, to show which file the
is currently being copied during a multiple-file copy.

getNote

```java
public
String
getNote()
```

Specifies the additional note that is displayed along with the
progress message.

**Returns:** a String specifying the note to display
**See Also:** setNote(java.lang.String)

---

#### getNote

public

String

getNote()

Specifies the additional note that is displayed along with the
progress message.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

for the

ProgressMonitor

**Specified by:** getAccessibleContext

in interface

Accessible
**Returns:** the

AccessibleContext

for the

ProgressMonitor
**Since:** 1.5

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

for the

ProgressMonitor

---


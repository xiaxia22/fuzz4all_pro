# Class ActivationDesc

**Source:** `java.rmi\java\rmi\activation\ActivationDesc.html`

### Class Description

```java
public final class
ActivationDesc

extends
Object

implements
Serializable
```

An activation descriptor contains the information necessary to
activate an object:

- the object's group identifier,

the object's fully-qualified class name,

the object's code location (the location of the class), a codebase URL
path,

the object's restart "mode", and,

a "marshalled" object that can contain object specific
initialization data.

A descriptor registered with the activation system can be used to
recreate/activate the object specified by the descriptor. The

MarshalledObject

in the object's descriptor is passed
as the second argument to the remote object's constructor for
object to use during reinitialization/activation.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ActivationDesc​(
String
className,

String
location,

MarshalledObject
<?> data)
throws
ActivationException

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

**Parameters:**
- className

- the object's fully package qualified class name
- location

- the object's code location (from where the class is
loaded)
- data

- the object's initialization (activation) data contained
in marshalled form.

**Throws:**
- ActivationException

- if the current group is nonexistent
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public ActivationDesc​(
String
className,

String
location,

MarshalledObject
<?> data,
boolean restart)
throws
ActivationException

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

**Parameters:**
- className

- the object's fully package qualified class name
- location

- the object's code location (from where the class is
loaded)
- data

- the object's initialization (activation) data contained
in marshalled form.
- restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.

**Throws:**
- ActivationException

- if the current group is nonexistent
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public ActivationDesc​(
ActivationGroupID
groupID,

String
className,

String
location,

MarshalledObject
<?> data)

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

**Parameters:**
- groupID

- the group's identifier (obtained from registering

ActivationSystem.registerGroup

method). The group
indicates the VM in which the object should be activated.
- className

- the object's fully package-qualified class name
- location

- the object's code location (from where the class is
loaded)
- data

- the object's initialization (activation) data contained
in marshalled form.

**Throws:**
- IllegalArgumentException

- if

groupID

is null
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

#### public ActivationDesc​(
ActivationGroupID
groupID,

String
className,

String
location,

MarshalledObject
<?> data,
boolean restart)

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

**Parameters:**
- groupID

- the group's identifier (obtained from registering

ActivationSystem.registerGroup

method). The group
indicates the VM in which the object should be activated.
- className

- the object's fully package-qualified class name
- location

- the object's code location (from where the class is
loaded)
- data

- the object's initialization (activation) data contained
in marshalled form.
- restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.

**Throws:**
- IllegalArgumentException

- if

groupID

is null
- UnsupportedOperationException

- if and only if activation is
not supported by this implementation

**Since:**
- 1.2

---

### Method Details

#### public
ActivationGroupID
getGroupID()

Returns the group identifier for the object specified by this
descriptor. A group provides a way to aggregate objects into a
single Java virtual machine. RMI creates/activates objects with
the same

groupID

in the same virtual machine.

**Returns:**
- the group identifier

**Since:**
- 1.2

---

#### public
String
getClassName()

Returns the class name for the object specified by this
descriptor.

**Returns:**
- the class name

**Since:**
- 1.2

---

#### public
String
getLocation()

Returns the code location for the object specified by
this descriptor.

**Returns:**
- the code location

**Since:**
- 1.2

---

#### public
MarshalledObject
<?> getData()

Returns a "marshalled object" containing intialization/activation
data for the object specified by this descriptor.

**Returns:**
- the object specific "initialization" data

**Since:**
- 1.2

---

#### public boolean getRestartMode()

Returns the "restart" mode of the object associated with
this activation descriptor.

**Returns:**
- true if the activatable object associated with this
activation descriptor is restarted via the activation
daemon when either the daemon comes up or the object's group
is restarted after an unexpected crash; otherwise it returns false,
meaning that the object is only activated on demand via a
method call. Note that if the restart mode is

true

, the
activator does not force an initial immediate activation of
a newly registered object; initial activation is lazy.

**Since:**
- 1.2

---

#### public boolean equals​(
Object
obj)

Compares two activation descriptors for content equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the Object to compare with

**Returns:**
- true if these Objects are equal; false otherwise.

**See Also:**
- Hashtable

**Since:**
- 1.2

---

#### public int hashCode()

Return the same hashCode for similar

ActivationDesc

s.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- an integer

**See Also:**
- Hashtable

---

### Additional Sections

#### Class ActivationDesc

java.lang.Object

- java.rmi.activation.ActivationDesc

java.rmi.activation.ActivationDesc

**All Implemented Interfaces:** Serializable

```java
public final class
ActivationDesc

extends
Object

implements
Serializable
```

An activation descriptor contains the information necessary to
activate an object:

- the object's group identifier,

the object's fully-qualified class name,

the object's code location (the location of the class), a codebase URL
path,

the object's restart "mode", and,

a "marshalled" object that can contain object specific
initialization data.

A descriptor registered with the activation system can be used to
recreate/activate the object specified by the descriptor. The

MarshalledObject

in the object's descriptor is passed
as the second argument to the remote object's constructor for
object to use during reinitialization/activation.

**Since:** 1.2
**See Also:** Activatable

,

Serialized Form

public final class

ActivationDesc

extends

Object

implements

Serializable

An activation descriptor contains the information necessary to
activate an object:

- the object's group identifier,

the object's fully-qualified class name,

the object's code location (the location of the class), a codebase URL
path,

the object's restart "mode", and,

a "marshalled" object that can contain object specific
initialization data.

A descriptor registered with the activation system can be used to
recreate/activate the object specified by the descriptor. The

MarshalledObject

in the object's descriptor is passed
as the second argument to the remote object's constructor for
object to use during reinitialization/activation.

the object's group identifier,

the object's fully-qualified class name,

the object's code location (the location of the class), a codebase URL
path,

the object's restart "mode", and,

a "marshalled" object that can contain object specific
initialization data.

A descriptor registered with the activation system can be used to
recreate/activate the object specified by the descriptor. The

MarshalledObject

in the object's descriptor is passed
as the second argument to the remote object's constructor for
object to use during reinitialization/activation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ActivationDesc

​(

String

className,

String

location,

MarshalledObject

<?> data)

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

.

ActivationDesc

​(

String

className,

String

location,

MarshalledObject

<?> data,
boolean restart)

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

.

ActivationDesc

​(

ActivationGroupID

groupID,

String

className,

String

location,

MarshalledObject

<?> data)

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

.

ActivationDesc

​(

ActivationGroupID

groupID,

String

className,

String

location,

MarshalledObject

<?> data,
boolean restart)

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares two activation descriptors for content equality.

String

getClassName

()

Returns the class name for the object specified by this
descriptor.

MarshalledObject

<?>

getData

()

Returns a "marshalled object" containing intialization/activation
data for the object specified by this descriptor.

ActivationGroupID

getGroupID

()

Returns the group identifier for the object specified by this
descriptor.

String

getLocation

()

Returns the code location for the object specified by
this descriptor.

boolean

getRestartMode

()

Returns the "restart" mode of the object associated with
this activation descriptor.

int

hashCode

()

Return the same hashCode for similar

ActivationDesc

s.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Constructor Summary

Constructors

Constructor

Description

ActivationDesc

​(

String

className,

String

location,

MarshalledObject

<?> data)

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

.

ActivationDesc

​(

String

className,

String

location,

MarshalledObject

<?> data,
boolean restart)

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

.

ActivationDesc

​(

ActivationGroupID

groupID,

String

className,

String

location,

MarshalledObject

<?> data)

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

.

ActivationDesc

​(

ActivationGroupID

groupID,

String

className,

String

location,

MarshalledObject

<?> data,
boolean restart)

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

.

---

#### Constructor Summary

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

.

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares two activation descriptors for content equality.

String

getClassName

()

Returns the class name for the object specified by this
descriptor.

MarshalledObject

<?>

getData

()

Returns a "marshalled object" containing intialization/activation
data for the object specified by this descriptor.

ActivationGroupID

getGroupID

()

Returns the group identifier for the object specified by this
descriptor.

String

getLocation

()

Returns the code location for the object specified by
this descriptor.

boolean

getRestartMode

()

Returns the "restart" mode of the object associated with
this activation descriptor.

int

hashCode

()

Return the same hashCode for similar

ActivationDesc

s.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Compares two activation descriptors for content equality.

Returns the class name for the object specified by this
descriptor.

Returns a "marshalled object" containing intialization/activation
data for the object specified by this descriptor.

Returns the group identifier for the object specified by this
descriptor.

Returns the code location for the object specified by
this descriptor.

Returns the "restart" mode of the object associated with
this activation descriptor.

Return the same hashCode for similar

ActivationDesc

s.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ActivationDesc

```java
public ActivationDesc​(
String
className,

String
location,

MarshalledObject
<?> data)
throws
ActivationException
```

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

**Parameters:** className

- the object's fully package qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Throws:** ActivationException

- if the current group is nonexistent
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- ActivationDesc

```java
public ActivationDesc​(
String
className,

String
location,

MarshalledObject
<?> data,
boolean restart)
throws
ActivationException
```

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

**Parameters:** className

- the object's fully package qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** ActivationException

- if the current group is nonexistent
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- ActivationDesc

```java
public ActivationDesc​(
ActivationGroupID
groupID,

String
className,

String
location,

MarshalledObject
<?> data)
```

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

**Parameters:** groupID

- the group's identifier (obtained from registering

ActivationSystem.registerGroup

method). The group
indicates the VM in which the object should be activated.
**Parameters:** className

- the object's fully package-qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Throws:** IllegalArgumentException

- if

groupID

is null
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- ActivationDesc

```java
public ActivationDesc​(
ActivationGroupID
groupID,

String
className,

String
location,

MarshalledObject
<?> data,
boolean restart)
```

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

**Parameters:** groupID

- the group's identifier (obtained from registering

ActivationSystem.registerGroup

method). The group
indicates the VM in which the object should be activated.
**Parameters:** className

- the object's fully package-qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** IllegalArgumentException

- if

groupID

is null
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getGroupID

```java
public
ActivationGroupID
getGroupID()
```

Returns the group identifier for the object specified by this
descriptor. A group provides a way to aggregate objects into a
single Java virtual machine. RMI creates/activates objects with
the same

groupID

in the same virtual machine.

**Returns:** the group identifier
**Since:** 1.2

- getClassName

```java
public
String
getClassName()
```

Returns the class name for the object specified by this
descriptor.

**Returns:** the class name
**Since:** 1.2

- getLocation

```java
public
String
getLocation()
```

Returns the code location for the object specified by
this descriptor.

**Returns:** the code location
**Since:** 1.2

- getData

```java
public
MarshalledObject
<?> getData()
```

Returns a "marshalled object" containing intialization/activation
data for the object specified by this descriptor.

**Returns:** the object specific "initialization" data
**Since:** 1.2

- getRestartMode

```java
public boolean getRestartMode()
```

Returns the "restart" mode of the object associated with
this activation descriptor.

**Returns:** true if the activatable object associated with this
activation descriptor is restarted via the activation
daemon when either the daemon comes up or the object's group
is restarted after an unexpected crash; otherwise it returns false,
meaning that the object is only activated on demand via a
method call. Note that if the restart mode is

true

, the
activator does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Since:** 1.2

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation descriptors for content equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

- hashCode

```java
public int hashCode()
```

Return the same hashCode for similar

ActivationDesc

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

Constructor Detail

- ActivationDesc

```java
public ActivationDesc​(
String
className,

String
location,

MarshalledObject
<?> data)
throws
ActivationException
```

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

**Parameters:** className

- the object's fully package qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Throws:** ActivationException

- if the current group is nonexistent
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- ActivationDesc

```java
public ActivationDesc​(
String
className,

String
location,

MarshalledObject
<?> data,
boolean restart)
throws
ActivationException
```

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

**Parameters:** className

- the object's fully package qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** ActivationException

- if the current group is nonexistent
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- ActivationDesc

```java
public ActivationDesc​(
ActivationGroupID
groupID,

String
className,

String
location,

MarshalledObject
<?> data)
```

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

**Parameters:** groupID

- the group's identifier (obtained from registering

ActivationSystem.registerGroup

method). The group
indicates the VM in which the object should be activated.
**Parameters:** className

- the object's fully package-qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Throws:** IllegalArgumentException

- if

groupID

is null
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

- ActivationDesc

```java
public ActivationDesc​(
ActivationGroupID
groupID,

String
className,

String
location,

MarshalledObject
<?> data,
boolean restart)
```

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

**Parameters:** groupID

- the group's identifier (obtained from registering

ActivationSystem.registerGroup

method). The group
indicates the VM in which the object should be activated.
**Parameters:** className

- the object's fully package-qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** IllegalArgumentException

- if

groupID

is null
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### Constructor Detail

ActivationDesc

```java
public ActivationDesc​(
String
className,

String
location,

MarshalledObject
<?> data)
throws
ActivationException
```

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

**Parameters:** className

- the object's fully package qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Throws:** ActivationException

- if the current group is nonexistent
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### ActivationDesc

public ActivationDesc​(

String

className,

String

location,

MarshalledObject

<?> data)
throws

ActivationException

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

ActivationDesc

```java
public ActivationDesc​(
String
className,

String
location,

MarshalledObject
<?> data,
boolean restart)
throws
ActivationException
```

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

**Parameters:** className

- the object's fully package qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** ActivationException

- if the current group is nonexistent
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### ActivationDesc

public ActivationDesc​(

String

className,

String

location,

MarshalledObject

<?> data,
boolean restart)
throws

ActivationException

Constructs an object descriptor for an object whose class name
is

className

, that can be loaded from the
code

location

and whose initialization
information is

data

. If this form of the constructor
is used, the

groupID

defaults to the current id for

ActivationGroup

for this VM. All objects with the
same

ActivationGroupID

are activated in the same VM.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

This constructor will throw

ActivationException

if
there is no current activation group for this VM. To create an

ActivationGroup

use the

ActivationGroup.createGroup

method.

ActivationDesc

```java
public ActivationDesc​(
ActivationGroupID
groupID,

String
className,

String
location,

MarshalledObject
<?> data)
```

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

**Parameters:** groupID

- the group's identifier (obtained from registering

ActivationSystem.registerGroup

method). The group
indicates the VM in which the object should be activated.
**Parameters:** className

- the object's fully package-qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Throws:** IllegalArgumentException

- if

groupID

is null
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### ActivationDesc

public ActivationDesc​(

ActivationGroupID

groupID,

String

className,

String

location,

MarshalledObject

<?> data)

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

Note that objects specified by a descriptor created with this
constructor will only be activated on demand (by default, the restart
mode is

false

). If an activatable object requires restart
services, use one of the

ActivationDesc

constructors that
takes a boolean parameter,

restart

.

ActivationDesc

```java
public ActivationDesc​(
ActivationGroupID
groupID,

String
className,

String
location,

MarshalledObject
<?> data,
boolean restart)
```

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

**Parameters:** groupID

- the group's identifier (obtained from registering

ActivationSystem.registerGroup

method). The group
indicates the VM in which the object should be activated.
**Parameters:** className

- the object's fully package-qualified class name
**Parameters:** location

- the object's code location (from where the class is
loaded)
**Parameters:** data

- the object's initialization (activation) data contained
in marshalled form.
**Parameters:** restart

- if true, the object is restarted (reactivated) when
either the activator is restarted or the object's activation group
is restarted after an unexpected crash; if false, the object is only
activated on demand. Specifying

restart

to be

true

does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Throws:** IllegalArgumentException

- if

groupID

is null
**Throws:** UnsupportedOperationException

- if and only if activation is
not supported by this implementation
**Since:** 1.2

---

#### ActivationDesc

public ActivationDesc​(

ActivationGroupID

groupID,

String

className,

String

location,

MarshalledObject

<?> data,
boolean restart)

Constructs an object descriptor for an object whose class name
is

className

that can be loaded from the
code

location

and whose initialization
information is

data

. All objects with the same

groupID

are activated in the same Java VM.

Method Detail

- getGroupID

```java
public
ActivationGroupID
getGroupID()
```

Returns the group identifier for the object specified by this
descriptor. A group provides a way to aggregate objects into a
single Java virtual machine. RMI creates/activates objects with
the same

groupID

in the same virtual machine.

**Returns:** the group identifier
**Since:** 1.2

- getClassName

```java
public
String
getClassName()
```

Returns the class name for the object specified by this
descriptor.

**Returns:** the class name
**Since:** 1.2

- getLocation

```java
public
String
getLocation()
```

Returns the code location for the object specified by
this descriptor.

**Returns:** the code location
**Since:** 1.2

- getData

```java
public
MarshalledObject
<?> getData()
```

Returns a "marshalled object" containing intialization/activation
data for the object specified by this descriptor.

**Returns:** the object specific "initialization" data
**Since:** 1.2

- getRestartMode

```java
public boolean getRestartMode()
```

Returns the "restart" mode of the object associated with
this activation descriptor.

**Returns:** true if the activatable object associated with this
activation descriptor is restarted via the activation
daemon when either the daemon comes up or the object's group
is restarted after an unexpected crash; otherwise it returns false,
meaning that the object is only activated on demand via a
method call. Note that if the restart mode is

true

, the
activator does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Since:** 1.2

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation descriptors for content equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

- hashCode

```java
public int hashCode()
```

Return the same hashCode for similar

ActivationDesc

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

---

#### Method Detail

getGroupID

```java
public
ActivationGroupID
getGroupID()
```

Returns the group identifier for the object specified by this
descriptor. A group provides a way to aggregate objects into a
single Java virtual machine. RMI creates/activates objects with
the same

groupID

in the same virtual machine.

**Returns:** the group identifier
**Since:** 1.2

---

#### getGroupID

public

ActivationGroupID

getGroupID()

Returns the group identifier for the object specified by this
descriptor. A group provides a way to aggregate objects into a
single Java virtual machine. RMI creates/activates objects with
the same

groupID

in the same virtual machine.

getClassName

```java
public
String
getClassName()
```

Returns the class name for the object specified by this
descriptor.

**Returns:** the class name
**Since:** 1.2

---

#### getClassName

public

String

getClassName()

Returns the class name for the object specified by this
descriptor.

getLocation

```java
public
String
getLocation()
```

Returns the code location for the object specified by
this descriptor.

**Returns:** the code location
**Since:** 1.2

---

#### getLocation

public

String

getLocation()

Returns the code location for the object specified by
this descriptor.

getData

```java
public
MarshalledObject
<?> getData()
```

Returns a "marshalled object" containing intialization/activation
data for the object specified by this descriptor.

**Returns:** the object specific "initialization" data
**Since:** 1.2

---

#### getData

public

MarshalledObject

<?> getData()

Returns a "marshalled object" containing intialization/activation
data for the object specified by this descriptor.

getRestartMode

```java
public boolean getRestartMode()
```

Returns the "restart" mode of the object associated with
this activation descriptor.

**Returns:** true if the activatable object associated with this
activation descriptor is restarted via the activation
daemon when either the daemon comes up or the object's group
is restarted after an unexpected crash; otherwise it returns false,
meaning that the object is only activated on demand via a
method call. Note that if the restart mode is

true

, the
activator does not force an initial immediate activation of
a newly registered object; initial activation is lazy.
**Since:** 1.2

---

#### getRestartMode

public boolean getRestartMode()

Returns the "restart" mode of the object associated with
this activation descriptor.

equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation descriptors for content equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

---

#### equals

public boolean equals​(

Object

obj)

Compares two activation descriptors for content equality.

hashCode

```java
public int hashCode()
```

Return the same hashCode for similar

ActivationDesc

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

---

#### hashCode

public int hashCode()

Return the same hashCode for similar

ActivationDesc

s.

---


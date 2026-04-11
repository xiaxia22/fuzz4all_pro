# Class ActivationGroupDesc

**Source:** `java.rmi\java\rmi\activation\ActivationGroupDesc.html`

### Class Description

```java
public final class
ActivationGroupDesc

extends
Object

implements
Serializable
```

An activation group descriptor contains the information necessary to
create/recreate an activation group in which to activate objects.
Such a descriptor contains:

- the group's class name,

the group's code location (the location of the group's class), and

a "marshalled" object that can contain group specific
initialization data.

The group's class must be a concrete subclass of

ActivationGroup

. A subclass of

ActivationGroup

is created/recreated via the

ActivationGroup.createGroup

static method that invokes
a special constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ActivationGroupDesc​(
Properties
overrides,

ActivationGroupDesc.CommandEnvironment
cmd)

Constructs a group descriptor that uses the system defaults for group
implementation and code location. Properties specify Java
environment overrides (which will override system properties in
the group implementation's VM). The command
environment can control the exact command/options used in
starting the child VM, or can be

null

to accept
rmid's default.

This constructor will create an

ActivationGroupDesc

with a

null

group class name, which indicates the system's
default

ActivationGroup

implementation.

**Parameters:**
- overrides

- the set of properties to set when the group is
recreated.
- cmd

- the controlling options for executing the VM in
another process (or

null

).

**Since:**
- 1.2

---

#### public ActivationGroupDesc​(
String
className,

String
location,

MarshalledObject
<?> data,

Properties
overrides,

ActivationGroupDesc.CommandEnvironment
cmd)

Specifies an alternate group implementation and execution
environment to be used for the group.

**Parameters:**
- className

- the group's package qualified class name or

null

. A

null

group class name indicates
the system's default

ActivationGroup

implementation.
- location

- the location from where to load the group's
class
- data

- the group's initialization data contained in
marshalled form (could contain properties, for example)
- overrides

- a properties map which will override those set
by default in the subprocess environment (will be translated
into

-D

options), or

null

.
- cmd

- the controlling options for executing the VM in
another process (or

null

).

**Since:**
- 1.2

---

### Method Details

#### public
String
getClassName()

Returns the group's class name (possibly

null

). A

null

group class name indicates the system's default

ActivationGroup

implementation.

**Returns:**
- the group's class name

**Since:**
- 1.2

---

#### public
String
getLocation()

Returns the group's code location.

**Returns:**
- the group's code location

**Since:**
- 1.2

---

#### public
MarshalledObject
<?> getData()

Returns the group's initialization data.

**Returns:**
- the group's initialization data

**Since:**
- 1.2

---

#### public
Properties
getPropertyOverrides()

Returns the group's property-override list.

**Returns:**
- the property-override list, or

null

**Since:**
- 1.2

---

#### public
ActivationGroupDesc.CommandEnvironment
getCommandEnvironment()

Returns the group's command-environment control object.

**Returns:**
- the command-environment object, or

null

**Since:**
- 1.2

---

#### public boolean equals​(
Object
obj)

Compares two activation group descriptors for content equality.

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

Produce identical numbers for similar

ActivationGroupDesc

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

#### Class ActivationGroupDesc

java.lang.Object

- java.rmi.activation.ActivationGroupDesc

java.rmi.activation.ActivationGroupDesc

**All Implemented Interfaces:** Serializable

```java
public final class
ActivationGroupDesc

extends
Object

implements
Serializable
```

An activation group descriptor contains the information necessary to
create/recreate an activation group in which to activate objects.
Such a descriptor contains:

- the group's class name,

the group's code location (the location of the group's class), and

a "marshalled" object that can contain group specific
initialization data.

The group's class must be a concrete subclass of

ActivationGroup

. A subclass of

ActivationGroup

is created/recreated via the

ActivationGroup.createGroup

static method that invokes
a special constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

**Since:** 1.2
**See Also:** ActivationGroup

,

ActivationGroupID

,

Serialized Form

public final class

ActivationGroupDesc

extends

Object

implements

Serializable

An activation group descriptor contains the information necessary to
create/recreate an activation group in which to activate objects.
Such a descriptor contains:

- the group's class name,

the group's code location (the location of the group's class), and

a "marshalled" object that can contain group specific
initialization data.

The group's class must be a concrete subclass of

ActivationGroup

. A subclass of

ActivationGroup

is created/recreated via the

ActivationGroup.createGroup

static method that invokes
a special constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

the group's class name,

the group's code location (the location of the group's class), and

a "marshalled" object that can contain group specific
initialization data.

The group's class must be a concrete subclass of

ActivationGroup

. A subclass of

ActivationGroup

is created/recreated via the

ActivationGroup.createGroup

static method that invokes
a special constructor that takes two arguments:

- the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

the group's

ActivationGroupID

, and

the group's initialization data (in a

java.rmi.MarshalledObject

)

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ActivationGroupDesc.CommandEnvironment

Startup options for ActivationGroup implementations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ActivationGroupDesc

​(

String

className,

String

location,

MarshalledObject

<?> data,

Properties

overrides,

ActivationGroupDesc.CommandEnvironment

cmd)

Specifies an alternate group implementation and execution
environment to be used for the group.

ActivationGroupDesc

​(

Properties

overrides,

ActivationGroupDesc.CommandEnvironment

cmd)

Constructs a group descriptor that uses the system defaults for group
implementation and code location.

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

Compares two activation group descriptors for content equality.

String

getClassName

()

Returns the group's class name (possibly

null

).

ActivationGroupDesc.CommandEnvironment

getCommandEnvironment

()

Returns the group's command-environment control object.

MarshalledObject

<?>

getData

()

Returns the group's initialization data.

String

getLocation

()

Returns the group's code location.

Properties

getPropertyOverrides

()

Returns the group's property-override list.

int

hashCode

()

Produce identical numbers for similar

ActivationGroupDesc

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ActivationGroupDesc.CommandEnvironment

Startup options for ActivationGroup implementations.

---

#### Nested Class Summary

Startup options for ActivationGroup implementations.

Constructor Summary

Constructors

Constructor

Description

ActivationGroupDesc

​(

String

className,

String

location,

MarshalledObject

<?> data,

Properties

overrides,

ActivationGroupDesc.CommandEnvironment

cmd)

Specifies an alternate group implementation and execution
environment to be used for the group.

ActivationGroupDesc

​(

Properties

overrides,

ActivationGroupDesc.CommandEnvironment

cmd)

Constructs a group descriptor that uses the system defaults for group
implementation and code location.

---

#### Constructor Summary

Specifies an alternate group implementation and execution
environment to be used for the group.

Constructs a group descriptor that uses the system defaults for group
implementation and code location.

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

Compares two activation group descriptors for content equality.

String

getClassName

()

Returns the group's class name (possibly

null

).

ActivationGroupDesc.CommandEnvironment

getCommandEnvironment

()

Returns the group's command-environment control object.

MarshalledObject

<?>

getData

()

Returns the group's initialization data.

String

getLocation

()

Returns the group's code location.

Properties

getPropertyOverrides

()

Returns the group's property-override list.

int

hashCode

()

Produce identical numbers for similar

ActivationGroupDesc

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

Compares two activation group descriptors for content equality.

Returns the group's class name (possibly

null

).

Returns the group's command-environment control object.

Returns the group's initialization data.

Returns the group's code location.

Returns the group's property-override list.

Produce identical numbers for similar

ActivationGroupDesc

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

- ActivationGroupDesc

```java
public ActivationGroupDesc​(
Properties
overrides,

ActivationGroupDesc.CommandEnvironment
cmd)
```

Constructs a group descriptor that uses the system defaults for group
implementation and code location. Properties specify Java
environment overrides (which will override system properties in
the group implementation's VM). The command
environment can control the exact command/options used in
starting the child VM, or can be

null

to accept
rmid's default.

This constructor will create an

ActivationGroupDesc

with a

null

group class name, which indicates the system's
default

ActivationGroup

implementation.

**Parameters:** overrides

- the set of properties to set when the group is
recreated.
**Parameters:** cmd

- the controlling options for executing the VM in
another process (or

null

).
**Since:** 1.2

- ActivationGroupDesc

```java
public ActivationGroupDesc​(
String
className,

String
location,

MarshalledObject
<?> data,

Properties
overrides,

ActivationGroupDesc.CommandEnvironment
cmd)
```

Specifies an alternate group implementation and execution
environment to be used for the group.

**Parameters:** className

- the group's package qualified class name or

null

. A

null

group class name indicates
the system's default

ActivationGroup

implementation.
**Parameters:** location

- the location from where to load the group's
class
**Parameters:** data

- the group's initialization data contained in
marshalled form (could contain properties, for example)
**Parameters:** overrides

- a properties map which will override those set
by default in the subprocess environment (will be translated
into

-D

options), or

null

.
**Parameters:** cmd

- the controlling options for executing the VM in
another process (or

null

).
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
public
String
getClassName()
```

Returns the group's class name (possibly

null

). A

null

group class name indicates the system's default

ActivationGroup

implementation.

**Returns:** the group's class name
**Since:** 1.2

- getLocation

```java
public
String
getLocation()
```

Returns the group's code location.

**Returns:** the group's code location
**Since:** 1.2

- getData

```java
public
MarshalledObject
<?> getData()
```

Returns the group's initialization data.

**Returns:** the group's initialization data
**Since:** 1.2

- getPropertyOverrides

```java
public
Properties
getPropertyOverrides()
```

Returns the group's property-override list.

**Returns:** the property-override list, or

null
**Since:** 1.2

- getCommandEnvironment

```java
public
ActivationGroupDesc.CommandEnvironment
getCommandEnvironment()
```

Returns the group's command-environment control object.

**Returns:** the command-environment object, or

null
**Since:** 1.2

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation group descriptors for content equality.

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

Produce identical numbers for similar

ActivationGroupDesc

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

Constructor Detail

- ActivationGroupDesc

```java
public ActivationGroupDesc​(
Properties
overrides,

ActivationGroupDesc.CommandEnvironment
cmd)
```

Constructs a group descriptor that uses the system defaults for group
implementation and code location. Properties specify Java
environment overrides (which will override system properties in
the group implementation's VM). The command
environment can control the exact command/options used in
starting the child VM, or can be

null

to accept
rmid's default.

This constructor will create an

ActivationGroupDesc

with a

null

group class name, which indicates the system's
default

ActivationGroup

implementation.

**Parameters:** overrides

- the set of properties to set when the group is
recreated.
**Parameters:** cmd

- the controlling options for executing the VM in
another process (or

null

).
**Since:** 1.2

- ActivationGroupDesc

```java
public ActivationGroupDesc​(
String
className,

String
location,

MarshalledObject
<?> data,

Properties
overrides,

ActivationGroupDesc.CommandEnvironment
cmd)
```

Specifies an alternate group implementation and execution
environment to be used for the group.

**Parameters:** className

- the group's package qualified class name or

null

. A

null

group class name indicates
the system's default

ActivationGroup

implementation.
**Parameters:** location

- the location from where to load the group's
class
**Parameters:** data

- the group's initialization data contained in
marshalled form (could contain properties, for example)
**Parameters:** overrides

- a properties map which will override those set
by default in the subprocess environment (will be translated
into

-D

options), or

null

.
**Parameters:** cmd

- the controlling options for executing the VM in
another process (or

null

).
**Since:** 1.2

---

#### Constructor Detail

ActivationGroupDesc

```java
public ActivationGroupDesc​(
Properties
overrides,

ActivationGroupDesc.CommandEnvironment
cmd)
```

Constructs a group descriptor that uses the system defaults for group
implementation and code location. Properties specify Java
environment overrides (which will override system properties in
the group implementation's VM). The command
environment can control the exact command/options used in
starting the child VM, or can be

null

to accept
rmid's default.

This constructor will create an

ActivationGroupDesc

with a

null

group class name, which indicates the system's
default

ActivationGroup

implementation.

**Parameters:** overrides

- the set of properties to set when the group is
recreated.
**Parameters:** cmd

- the controlling options for executing the VM in
another process (or

null

).
**Since:** 1.2

---

#### ActivationGroupDesc

public ActivationGroupDesc​(

Properties

overrides,

ActivationGroupDesc.CommandEnvironment

cmd)

Constructs a group descriptor that uses the system defaults for group
implementation and code location. Properties specify Java
environment overrides (which will override system properties in
the group implementation's VM). The command
environment can control the exact command/options used in
starting the child VM, or can be

null

to accept
rmid's default.

This constructor will create an

ActivationGroupDesc

with a

null

group class name, which indicates the system's
default

ActivationGroup

implementation.

This constructor will create an

ActivationGroupDesc

with a

null

group class name, which indicates the system's
default

ActivationGroup

implementation.

ActivationGroupDesc

```java
public ActivationGroupDesc​(
String
className,

String
location,

MarshalledObject
<?> data,

Properties
overrides,

ActivationGroupDesc.CommandEnvironment
cmd)
```

Specifies an alternate group implementation and execution
environment to be used for the group.

**Parameters:** className

- the group's package qualified class name or

null

. A

null

group class name indicates
the system's default

ActivationGroup

implementation.
**Parameters:** location

- the location from where to load the group's
class
**Parameters:** data

- the group's initialization data contained in
marshalled form (could contain properties, for example)
**Parameters:** overrides

- a properties map which will override those set
by default in the subprocess environment (will be translated
into

-D

options), or

null

.
**Parameters:** cmd

- the controlling options for executing the VM in
another process (or

null

).
**Since:** 1.2

---

#### ActivationGroupDesc

public ActivationGroupDesc​(

String

className,

String

location,

MarshalledObject

<?> data,

Properties

overrides,

ActivationGroupDesc.CommandEnvironment

cmd)

Specifies an alternate group implementation and execution
environment to be used for the group.

Method Detail

- getClassName

```java
public
String
getClassName()
```

Returns the group's class name (possibly

null

). A

null

group class name indicates the system's default

ActivationGroup

implementation.

**Returns:** the group's class name
**Since:** 1.2

- getLocation

```java
public
String
getLocation()
```

Returns the group's code location.

**Returns:** the group's code location
**Since:** 1.2

- getData

```java
public
MarshalledObject
<?> getData()
```

Returns the group's initialization data.

**Returns:** the group's initialization data
**Since:** 1.2

- getPropertyOverrides

```java
public
Properties
getPropertyOverrides()
```

Returns the group's property-override list.

**Returns:** the property-override list, or

null
**Since:** 1.2

- getCommandEnvironment

```java
public
ActivationGroupDesc.CommandEnvironment
getCommandEnvironment()
```

Returns the group's command-environment control object.

**Returns:** the command-environment object, or

null
**Since:** 1.2

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation group descriptors for content equality.

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

Produce identical numbers for similar

ActivationGroupDesc

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

---

#### Method Detail

getClassName

```java
public
String
getClassName()
```

Returns the group's class name (possibly

null

). A

null

group class name indicates the system's default

ActivationGroup

implementation.

**Returns:** the group's class name
**Since:** 1.2

---

#### getClassName

public

String

getClassName()

Returns the group's class name (possibly

null

). A

null

group class name indicates the system's default

ActivationGroup

implementation.

getLocation

```java
public
String
getLocation()
```

Returns the group's code location.

**Returns:** the group's code location
**Since:** 1.2

---

#### getLocation

public

String

getLocation()

Returns the group's code location.

getData

```java
public
MarshalledObject
<?> getData()
```

Returns the group's initialization data.

**Returns:** the group's initialization data
**Since:** 1.2

---

#### getData

public

MarshalledObject

<?> getData()

Returns the group's initialization data.

getPropertyOverrides

```java
public
Properties
getPropertyOverrides()
```

Returns the group's property-override list.

**Returns:** the property-override list, or

null
**Since:** 1.2

---

#### getPropertyOverrides

public

Properties

getPropertyOverrides()

Returns the group's property-override list.

getCommandEnvironment

```java
public
ActivationGroupDesc.CommandEnvironment
getCommandEnvironment()
```

Returns the group's command-environment control object.

**Returns:** the command-environment object, or

null
**Since:** 1.2

---

#### getCommandEnvironment

public

ActivationGroupDesc.CommandEnvironment

getCommandEnvironment()

Returns the group's command-environment control object.

equals

```java
public boolean equals​(
Object
obj)
```

Compares two activation group descriptors for content equality.

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

Compares two activation group descriptors for content equality.

hashCode

```java
public int hashCode()
```

Produce identical numbers for similar

ActivationGroupDesc

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

---

#### hashCode

public int hashCode()

Produce identical numbers for similar

ActivationGroupDesc

s.

---


# Interface ActivationInstantiator

**Source:** `java.rmi\java\rmi\activation\ActivationInstantiator.html`

### Class Description

```java
public interface
ActivationInstantiator

extends
Remote
```

An

ActivationInstantiator

is responsible for creating
instances of "activatable" objects. A concrete subclass of

ActivationGroup

implements the

newInstance

method to handle creating objects within the group.

**All Superinterfaces:** Remote

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### MarshalledObject
<? extends
Remote
> newInstance​(
ActivationID
id,

ActivationDesc
desc)
throws
ActivationException
,

RemoteException

The activator calls an instantiator's

newInstance

method in order to recreate in that group an object with the
activation identifier,

id

, and descriptor,

desc

. The instantiator is responsible for:

- determining the class for the object using the descriptor's

getClassName

method,

loading the class from the code location obtained from the
descriptor (using the

getLocation

method),

creating an instance of the class by invoking the special
"activation" constructor of the object's class that takes two
arguments: the object's

ActivationID

, and the

MarshalledObject

containing object specific
initialization data, and

returning a MarshalledObject containing the stub for the
remote object it created.

In order for activation to be successful, one of the following requirements
must be met, otherwise

ActivationException

is thrown:

- The class to be activated and the special activation constructor are both public,
and the class resides in a package that is

exported

to at least the

java.rmi

module; or

The class to be activated resides in a package that is

open

to at least the

java.rmi

module.

**Parameters:**
- id

- the object's activation identifier
- desc

- the object's descriptor

**Returns:**
- a marshalled object containing the serialized
representation of remote object's stub

**Throws:**
- ActivationException

- if object activation fails
- RemoteException

- if remote call fails

**Since:**
- 1.2

---

### Additional Sections

#### Interface ActivationInstantiator

**All Superinterfaces:** Remote

**All Known Implementing Classes:** ActivationGroup

,

ActivationGroup_Stub

```java
public interface
ActivationInstantiator

extends
Remote
```

An

ActivationInstantiator

is responsible for creating
instances of "activatable" objects. A concrete subclass of

ActivationGroup

implements the

newInstance

method to handle creating objects within the group.

**Since:** 1.2
**See Also:** ActivationGroup

public interface

ActivationInstantiator

extends

Remote

An

ActivationInstantiator

is responsible for creating
instances of "activatable" objects. A concrete subclass of

ActivationGroup

implements the

newInstance

method to handle creating objects within the group.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MarshalledObject

<? extends

Remote

>

newInstance

​(

ActivationID

id,

ActivationDesc

desc)

The activator calls an instantiator's

newInstance

method in order to recreate in that group an object with the
activation identifier,

id

, and descriptor,

desc

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MarshalledObject

<? extends

Remote

>

newInstance

​(

ActivationID

id,

ActivationDesc

desc)

The activator calls an instantiator's

newInstance

method in order to recreate in that group an object with the
activation identifier,

id

, and descriptor,

desc

.

---

#### Method Summary

The activator calls an instantiator's

newInstance

method in order to recreate in that group an object with the
activation identifier,

id

, and descriptor,

desc

.

============ METHOD DETAIL ==========

- Method Detail

- newInstance

```java
MarshalledObject
<? extends
Remote
> newInstance​(
ActivationID
id,

ActivationDesc
desc)
throws
ActivationException
,

RemoteException
```

The activator calls an instantiator's

newInstance

method in order to recreate in that group an object with the
activation identifier,

id

, and descriptor,

desc

. The instantiator is responsible for:

- determining the class for the object using the descriptor's

getClassName

method,

loading the class from the code location obtained from the
descriptor (using the

getLocation

method),

creating an instance of the class by invoking the special
"activation" constructor of the object's class that takes two
arguments: the object's

ActivationID

, and the

MarshalledObject

containing object specific
initialization data, and

returning a MarshalledObject containing the stub for the
remote object it created.

In order for activation to be successful, one of the following requirements
must be met, otherwise

ActivationException

is thrown:

- The class to be activated and the special activation constructor are both public,
and the class resides in a package that is

exported

to at least the

java.rmi

module; or

The class to be activated resides in a package that is

open

to at least the

java.rmi

module.

**Parameters:** id

- the object's activation identifier
**Parameters:** desc

- the object's descriptor
**Returns:** a marshalled object containing the serialized
representation of remote object's stub
**Throws:** ActivationException

- if object activation fails
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

Method Detail

- newInstance

```java
MarshalledObject
<? extends
Remote
> newInstance​(
ActivationID
id,

ActivationDesc
desc)
throws
ActivationException
,

RemoteException
```

The activator calls an instantiator's

newInstance

method in order to recreate in that group an object with the
activation identifier,

id

, and descriptor,

desc

. The instantiator is responsible for:

- determining the class for the object using the descriptor's

getClassName

method,

loading the class from the code location obtained from the
descriptor (using the

getLocation

method),

creating an instance of the class by invoking the special
"activation" constructor of the object's class that takes two
arguments: the object's

ActivationID

, and the

MarshalledObject

containing object specific
initialization data, and

returning a MarshalledObject containing the stub for the
remote object it created.

In order for activation to be successful, one of the following requirements
must be met, otherwise

ActivationException

is thrown:

- The class to be activated and the special activation constructor are both public,
and the class resides in a package that is

exported

to at least the

java.rmi

module; or

The class to be activated resides in a package that is

open

to at least the

java.rmi

module.

**Parameters:** id

- the object's activation identifier
**Parameters:** desc

- the object's descriptor
**Returns:** a marshalled object containing the serialized
representation of remote object's stub
**Throws:** ActivationException

- if object activation fails
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### Method Detail

newInstance

```java
MarshalledObject
<? extends
Remote
> newInstance​(
ActivationID
id,

ActivationDesc
desc)
throws
ActivationException
,

RemoteException
```

The activator calls an instantiator's

newInstance

method in order to recreate in that group an object with the
activation identifier,

id

, and descriptor,

desc

. The instantiator is responsible for:

- determining the class for the object using the descriptor's

getClassName

method,

loading the class from the code location obtained from the
descriptor (using the

getLocation

method),

creating an instance of the class by invoking the special
"activation" constructor of the object's class that takes two
arguments: the object's

ActivationID

, and the

MarshalledObject

containing object specific
initialization data, and

returning a MarshalledObject containing the stub for the
remote object it created.

In order for activation to be successful, one of the following requirements
must be met, otherwise

ActivationException

is thrown:

- The class to be activated and the special activation constructor are both public,
and the class resides in a package that is

exported

to at least the

java.rmi

module; or

The class to be activated resides in a package that is

open

to at least the

java.rmi

module.

**Parameters:** id

- the object's activation identifier
**Parameters:** desc

- the object's descriptor
**Returns:** a marshalled object containing the serialized
representation of remote object's stub
**Throws:** ActivationException

- if object activation fails
**Throws:** RemoteException

- if remote call fails
**Since:** 1.2

---

#### newInstance

MarshalledObject

<? extends

Remote

> newInstance​(

ActivationID

id,

ActivationDesc

desc)
throws

ActivationException

,

RemoteException

The activator calls an instantiator's

newInstance

method in order to recreate in that group an object with the
activation identifier,

id

, and descriptor,

desc

. The instantiator is responsible for:

- determining the class for the object using the descriptor's

getClassName

method,

loading the class from the code location obtained from the
descriptor (using the

getLocation

method),

creating an instance of the class by invoking the special
"activation" constructor of the object's class that takes two
arguments: the object's

ActivationID

, and the

MarshalledObject

containing object specific
initialization data, and

returning a MarshalledObject containing the stub for the
remote object it created.

In order for activation to be successful, one of the following requirements
must be met, otherwise

ActivationException

is thrown:

- The class to be activated and the special activation constructor are both public,
and the class resides in a package that is

exported

to at least the

java.rmi

module; or

The class to be activated resides in a package that is

open

to at least the

java.rmi

module.

determining the class for the object using the descriptor's

getClassName

method,

loading the class from the code location obtained from the
descriptor (using the

getLocation

method),

creating an instance of the class by invoking the special
"activation" constructor of the object's class that takes two
arguments: the object's

ActivationID

, and the

MarshalledObject

containing object specific
initialization data, and

returning a MarshalledObject containing the stub for the
remote object it created.

In order for activation to be successful, one of the following requirements
must be met, otherwise

ActivationException

is thrown:

- The class to be activated and the special activation constructor are both public,
and the class resides in a package that is

exported

to at least the

java.rmi

module; or

The class to be activated resides in a package that is

open

to at least the

java.rmi

module.

The class to be activated and the special activation constructor are both public,
and the class resides in a package that is

exported

to at least the

java.rmi

module; or

The class to be activated resides in a package that is

open

to at least the

java.rmi

module.

---


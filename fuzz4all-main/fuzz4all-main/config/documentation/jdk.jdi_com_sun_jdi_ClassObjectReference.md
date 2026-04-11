# Interface ClassObjectReference

**Source:** `jdk.jdi\com\sun\jdi\ClassObjectReference.html`

### Class Description

```java
public interface
ClassObjectReference

extends
ObjectReference
```

An instance of java.lang.Class from the target VM.
Use this interface to access type information
for the class, array, or interface that this object reflects.

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ReferenceType
reflectedType()

Returns the

ReferenceType

corresponding to this
class object. The returned type can be used to obtain
detailed information about the class.

**Returns:**
- the

ReferenceType

reflected by this class object.

---

### Additional Sections

#### Interface ClassObjectReference

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

```java
public interface
ClassObjectReference

extends
ObjectReference
```

An instance of java.lang.Class from the target VM.
Use this interface to access type information
for the class, array, or interface that this object reflects.

**Since:** 1.3
**See Also:** ReferenceType

public interface

ClassObjectReference

extends

ObjectReference

An instance of java.lang.Class from the target VM.
Use this interface to access type information
for the class, array, or interface that this object reflects.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ReferenceType

reflectedType

()

Returns the

ReferenceType

corresponding to this
class object.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

- Methods declared in interface com.sun.jdi.

Value

type

Field Summary

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Field Summary

Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Fields declared in interface com.sun.jdi. ObjectReference

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ReferenceType

reflectedType

()

Returns the

ReferenceType

corresponding to this
class object.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

- Methods declared in interface com.sun.jdi.

Value

type

---

#### Method Summary

Returns the

ReferenceType

corresponding to this
class object.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

---

#### Methods declared in interface com.sun.jdi. ObjectReference

Methods declared in interface com.sun.jdi.

Value

type

---

#### Methods declared in interface com.sun.jdi. Value

============ METHOD DETAIL ==========

- Method Detail

- reflectedType

```java
ReferenceType
reflectedType()
```

Returns the

ReferenceType

corresponding to this
class object. The returned type can be used to obtain
detailed information about the class.

**Returns:** the

ReferenceType

reflected by this class object.

Method Detail

- reflectedType

```java
ReferenceType
reflectedType()
```

Returns the

ReferenceType

corresponding to this
class object. The returned type can be used to obtain
detailed information about the class.

**Returns:** the

ReferenceType

reflected by this class object.

---

#### Method Detail

reflectedType

```java
ReferenceType
reflectedType()
```

Returns the

ReferenceType

corresponding to this
class object. The returned type can be used to obtain
detailed information about the class.

**Returns:** the

ReferenceType

reflected by this class object.

---

#### reflectedType

ReferenceType

reflectedType()

Returns the

ReferenceType

corresponding to this
class object. The returned type can be used to obtain
detailed information about the class.

---


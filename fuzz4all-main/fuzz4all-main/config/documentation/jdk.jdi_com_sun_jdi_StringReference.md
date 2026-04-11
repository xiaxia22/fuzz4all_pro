# Interface StringReference

**Source:** `jdk.jdi\com\sun\jdi\StringReference.html`

### Class Description

```java
public interface
StringReference

extends
ObjectReference
```

A string object from the target VM.
A StringReference is an

ObjectReference

with additional
access to string-specific information from the target VM.

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

#### String
value()

Returns the StringReference as a String. The returned string
is the equivalent of the mirrored string, but is an entity in the
client VM and can be manipulated like any other string.

**Returns:**
- the string value.

---

### Additional Sections

#### Interface StringReference

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

```java
public interface
StringReference

extends
ObjectReference
```

A string object from the target VM.
A StringReference is an

ObjectReference

with additional
access to string-specific information from the target VM.

**Since:** 1.3

public interface

StringReference

extends

ObjectReference

A string object from the target VM.
A StringReference is an

ObjectReference

with additional
access to string-specific information from the target VM.

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

String

value

()

Returns the StringReference as a String.

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

String

value

()

Returns the StringReference as a String.

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

Returns the StringReference as a String.

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

- value

```java
String
value()
```

Returns the StringReference as a String. The returned string
is the equivalent of the mirrored string, but is an entity in the
client VM and can be manipulated like any other string.

**Returns:** the string value.

Method Detail

- value

```java
String
value()
```

Returns the StringReference as a String. The returned string
is the equivalent of the mirrored string, but is an entity in the
client VM and can be manipulated like any other string.

**Returns:** the string value.

---

#### Method Detail

value

```java
String
value()
```

Returns the StringReference as a String. The returned string
is the equivalent of the mirrored string, but is an entity in the
client VM and can be manipulated like any other string.

**Returns:** the string value.

---

#### value

String

value()

Returns the StringReference as a String. The returned string
is the equivalent of the mirrored string, but is an entity in the
client VM and can be manipulated like any other string.

---


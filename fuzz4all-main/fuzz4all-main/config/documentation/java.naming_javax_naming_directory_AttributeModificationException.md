# Class AttributeModificationException

**Source:** `java.naming\javax\naming\directory\AttributeModificationException.html`

### Class Description

```java
public class
AttributeModificationException

extends
NamingException
```

This exception is thrown when an attempt is
made to add, or remove, or modify an attribute, its identifier,
or its values that conflicts with the attribute's (schema) definition
or the attribute's state.
It is thrown in response to DirContext.modifyAttributes().
It contains a list of modifications that have not been performed, in the
order that they were supplied to modifyAttributes().
If the list is null, none of the modifications were performed successfully.

An AttributeModificationException instance is not synchronized
against concurrent multithreaded access. Multiple threads trying
to access and modify a single AttributeModification instance
should lock the object.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AttributeModificationException​(
String
explanation)

Constructs a new instance of AttributeModificationException using
an explanation. All other fields are set to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.
If null, this exception has no detail message.

**See Also:**
- Throwable.getMessage()

---

#### public AttributeModificationException()

Constructs a new instance of AttributeModificationException.
All fields are set to null.

---

### Method Details

#### public void setUnexecutedModifications​(
ModificationItem
[] e)

Sets the unexecuted modification list to be e.
Items in the list must appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

**Parameters:**
- e

- The possibly null list of unexecuted modifications.

**See Also:**
- getUnexecutedModifications()

---

#### public
ModificationItem
[] getUnexecutedModifications()

Retrieves the unexecuted modification list.
Items in the list appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

**Returns:**
- The possibly null unexecuted modification list.

**See Also:**
- setUnexecutedModifications(javax.naming.directory.ModificationItem[])

---

#### public
String
toString()

The string representation of this exception consists of
information about where the error occurred, and
the first unexecuted modification.
This string is meant for debugging and not mean to be interpreted
programmatically.

**Overrides:**
- toString

in class

NamingException

**Returns:**
- The non-null string representation of this exception.

---

### Additional Sections

#### Class AttributeModificationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.AttributeModificationException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.AttributeModificationException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.directory.AttributeModificationException

javax.naming.NamingException

- javax.naming.directory.AttributeModificationException

javax.naming.directory.AttributeModificationException

**All Implemented Interfaces:** Serializable

```java
public class
AttributeModificationException

extends
NamingException
```

This exception is thrown when an attempt is
made to add, or remove, or modify an attribute, its identifier,
or its values that conflicts with the attribute's (schema) definition
or the attribute's state.
It is thrown in response to DirContext.modifyAttributes().
It contains a list of modifications that have not been performed, in the
order that they were supplied to modifyAttributes().
If the list is null, none of the modifications were performed successfully.

An AttributeModificationException instance is not synchronized
against concurrent multithreaded access. Multiple threads trying
to access and modify a single AttributeModification instance
should lock the object.

**Since:** 1.3
**See Also:** DirContext.modifyAttributes(javax.naming.Name, int, javax.naming.directory.Attributes)

,

Serialized Form

public class

AttributeModificationException

extends

NamingException

This exception is thrown when an attempt is
made to add, or remove, or modify an attribute, its identifier,
or its values that conflicts with the attribute's (schema) definition
or the attribute's state.
It is thrown in response to DirContext.modifyAttributes().
It contains a list of modifications that have not been performed, in the
order that they were supplied to modifyAttributes().
If the list is null, none of the modifications were performed successfully.

An AttributeModificationException instance is not synchronized
against concurrent multithreaded access. Multiple threads trying
to access and modify a single AttributeModification instance
should lock the object.

An AttributeModificationException instance is not synchronized
against concurrent multithreaded access. Multiple threads trying
to access and modify a single AttributeModification instance
should lock the object.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AttributeModificationException

()

Constructs a new instance of AttributeModificationException.

AttributeModificationException

​(

String

explanation)

Constructs a new instance of AttributeModificationException using
an explanation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ModificationItem

[]

getUnexecutedModifications

()

Retrieves the unexecuted modification list.

void

setUnexecutedModifications

​(

ModificationItem

[] e)

Sets the unexecuted modification list to be e.

String

toString

()

The string representation of this exception consists of
information about where the error occurred, and
the first unexecuted modification.

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

wait

,

wait

,

wait

Field Summary

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Field Summary

Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Fields declared in class javax.naming. NamingException

Constructor Summary

Constructors

Constructor

Description

AttributeModificationException

()

Constructs a new instance of AttributeModificationException.

AttributeModificationException

​(

String

explanation)

Constructs a new instance of AttributeModificationException using
an explanation.

---

#### Constructor Summary

Constructs a new instance of AttributeModificationException.

Constructs a new instance of AttributeModificationException using
an explanation.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ModificationItem

[]

getUnexecutedModifications

()

Retrieves the unexecuted modification list.

void

setUnexecutedModifications

​(

ModificationItem

[] e)

Sets the unexecuted modification list to be e.

String

toString

()

The string representation of this exception consists of
information about where the error occurred, and
the first unexecuted modification.

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

wait

,

wait

,

wait

---

#### Method Summary

Retrieves the unexecuted modification list.

Sets the unexecuted modification list to be e.

The string representation of this exception consists of
information about where the error occurred, and
the first unexecuted modification.

Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

---

#### Methods declared in class javax.naming. NamingException

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AttributeModificationException

```java
public AttributeModificationException​(
String
explanation)
```

Constructs a new instance of AttributeModificationException using
an explanation. All other fields are set to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
If null, this exception has no detail message.
**See Also:** Throwable.getMessage()

- AttributeModificationException

```java
public AttributeModificationException()
```

Constructs a new instance of AttributeModificationException.
All fields are set to null.

============ METHOD DETAIL ==========

- Method Detail

- setUnexecutedModifications

```java
public void setUnexecutedModifications​(
ModificationItem
[] e)
```

Sets the unexecuted modification list to be e.
Items in the list must appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

**Parameters:** e

- The possibly null list of unexecuted modifications.
**See Also:** getUnexecutedModifications()

- getUnexecutedModifications

```java
public
ModificationItem
[] getUnexecutedModifications()
```

Retrieves the unexecuted modification list.
Items in the list appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

**Returns:** The possibly null unexecuted modification list.
**See Also:** setUnexecutedModifications(javax.naming.directory.ModificationItem[])

- toString

```java
public
String
toString()
```

The string representation of this exception consists of
information about where the error occurred, and
the first unexecuted modification.
This string is meant for debugging and not mean to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Returns:** The non-null string representation of this exception.

Constructor Detail

- AttributeModificationException

```java
public AttributeModificationException​(
String
explanation)
```

Constructs a new instance of AttributeModificationException using
an explanation. All other fields are set to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
If null, this exception has no detail message.
**See Also:** Throwable.getMessage()

- AttributeModificationException

```java
public AttributeModificationException()
```

Constructs a new instance of AttributeModificationException.
All fields are set to null.

---

#### Constructor Detail

AttributeModificationException

```java
public AttributeModificationException​(
String
explanation)
```

Constructs a new instance of AttributeModificationException using
an explanation. All other fields are set to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
If null, this exception has no detail message.
**See Also:** Throwable.getMessage()

---

#### AttributeModificationException

public AttributeModificationException​(

String

explanation)

Constructs a new instance of AttributeModificationException using
an explanation. All other fields are set to null.

AttributeModificationException

```java
public AttributeModificationException()
```

Constructs a new instance of AttributeModificationException.
All fields are set to null.

---

#### AttributeModificationException

public AttributeModificationException()

Constructs a new instance of AttributeModificationException.
All fields are set to null.

Method Detail

- setUnexecutedModifications

```java
public void setUnexecutedModifications​(
ModificationItem
[] e)
```

Sets the unexecuted modification list to be e.
Items in the list must appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

**Parameters:** e

- The possibly null list of unexecuted modifications.
**See Also:** getUnexecutedModifications()

- getUnexecutedModifications

```java
public
ModificationItem
[] getUnexecutedModifications()
```

Retrieves the unexecuted modification list.
Items in the list appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

**Returns:** The possibly null unexecuted modification list.
**See Also:** setUnexecutedModifications(javax.naming.directory.ModificationItem[])

- toString

```java
public
String
toString()
```

The string representation of this exception consists of
information about where the error occurred, and
the first unexecuted modification.
This string is meant for debugging and not mean to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Returns:** The non-null string representation of this exception.

---

#### Method Detail

setUnexecutedModifications

```java
public void setUnexecutedModifications​(
ModificationItem
[] e)
```

Sets the unexecuted modification list to be e.
Items in the list must appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

**Parameters:** e

- The possibly null list of unexecuted modifications.
**See Also:** getUnexecutedModifications()

---

#### setUnexecutedModifications

public void setUnexecutedModifications​(

ModificationItem

[] e)

Sets the unexecuted modification list to be e.
Items in the list must appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

getUnexecutedModifications

```java
public
ModificationItem
[] getUnexecutedModifications()
```

Retrieves the unexecuted modification list.
Items in the list appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

**Returns:** The possibly null unexecuted modification list.
**See Also:** setUnexecutedModifications(javax.naming.directory.ModificationItem[])

---

#### getUnexecutedModifications

public

ModificationItem

[] getUnexecutedModifications()

Retrieves the unexecuted modification list.
Items in the list appear in the same order in which they were
originally supplied in DirContext.modifyAttributes().
The first item in the list is the first one that was not executed.
If this list is null, none of the operations originally submitted
to modifyAttributes() were executed.

toString

```java
public
String
toString()
```

The string representation of this exception consists of
information about where the error occurred, and
the first unexecuted modification.
This string is meant for debugging and not mean to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Returns:** The non-null string representation of this exception.

---

#### toString

public

String

toString()

The string representation of this exception consists of
information about where the error occurred, and
the first unexecuted modification.
This string is meant for debugging and not mean to be interpreted
programmatically.

---


# Class LinkException

**Source:** `java.naming\javax\naming\LinkException.html`

### Class Description

```java
public class
LinkException

extends
NamingException
```

This exception is used to describe problems encountered while resolving links.
Additional information is added to the base NamingException for pinpointing
the problem with the link.

Analogously to how NamingException captures name resolution information,
LinkException captures "link"-name resolution information pinpointing
the problem encountered while resolving a link. All these fields may
be null.

- Link Resolved Name. Portion of link name that has been resolved.

Link Resolved Object. Object to which resolution of link name proceeded.

Link Remaining Name. Portion of link name that has not been resolved.

Link Explanation. Detail explaining why link resolution failed.

A LinkException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single LinkException instance should lock the object.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Name
linkResolvedName

Contains the part of the link that has been successfully resolved.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:**
- getLinkResolvedName()

,

setLinkResolvedName(javax.naming.Name)

---

#### protected
Object
linkResolvedObj

Contains the object to which resolution of the part of the link was successful.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:**
- getLinkResolvedObj()

,

setLinkResolvedObj(java.lang.Object)

---

#### protected
Name
linkRemainingName

Contains the remaining link name that has not been resolved yet.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:**
- getLinkRemainingName()

,

setLinkRemainingName(javax.naming.Name)

---

#### protected
String
linkExplanation

Contains the exception of why resolution of the link failed.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:**
- getLinkExplanation()

,

setLinkExplanation(java.lang.String)

---

### Constructor Details

#### public LinkException​(
String
explanation)

Constructs a new instance of LinkException with an explanation.
All the other fields are initialized to null.

**Parameters:**
- explanation

- A possibly null string containing additional
detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public LinkException()

Constructs a new instance of LinkException.
All the non-link-related and link-related fields are initialized to null.

---

### Method Details

#### public
Name
getLinkResolvedName()

Retrieves the leading portion of the link name that was resolved
successfully.

**Returns:**
- The part of the link name that was resolved successfully.
It is a composite name. It can be null, which means
the link resolved name field has not been set.

**See Also:**
- getLinkResolvedObj()

,

setLinkResolvedName(javax.naming.Name)

---

#### public
Name
getLinkRemainingName()

Retrieves the remaining unresolved portion of the link name.

**Returns:**
- The part of the link name that has not been resolved.
It is a composite name. It can be null, which means
the link remaining name field has not been set.

**See Also:**
- setLinkRemainingName(javax.naming.Name)

---

#### public
Object
getLinkResolvedObj()

Retrieves the object to which resolution was successful.
This is the object to which the resolved link name is bound.

**Returns:**
- The possibly null object that was resolved so far.
If null, it means the link resolved object field has not been set.

**See Also:**
- getLinkResolvedName()

,

setLinkResolvedObj(java.lang.Object)

---

#### public
String
getLinkExplanation()

Retrieves the explanation associated with the problem encountered
when resolving a link.

**Returns:**
- The possibly null detail string explaining more about the problem
with resolving a link.
If null, it means there is no
link detail message for this exception.

**See Also:**
- setLinkExplanation(java.lang.String)

---

#### public void setLinkExplanation​(
String
msg)

Sets the explanation associated with the problem encountered
when resolving a link.

**Parameters:**
- msg

- The possibly null detail string explaining more about the problem
with resolving a link. If null, it means no detail will be recorded.

**See Also:**
- getLinkExplanation()

---

#### public void setLinkResolvedName​(
Name
name)

Sets the resolved link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

**Parameters:**
- name

- The name to set resolved link name to. This can be null.
If null, it sets the link resolved name field to null.

**See Also:**
- getLinkResolvedName()

---

#### public void setLinkRemainingName​(
Name
name)

Sets the remaining link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

**Parameters:**
- name

- The name to set remaining link name to. This can be null.
If null, it sets the remaining name field to null.

**See Also:**
- getLinkRemainingName()

---

#### public void setLinkResolvedObj​(
Object
obj)

Sets the link resolved object field of this exception.
This indicates the last successfully resolved object of link name.

**Parameters:**
- obj

- The object to set link resolved object to. This can be null.
If null, the link resolved object field is set to null.

**See Also:**
- getLinkResolvedObj()

---

#### public
String
toString()

Generates the string representation of this exception.
This string consists of the NamingException information plus
the link's remaining name.
This string is used for debugging and not meant to be interpreted
programmatically.

**Overrides:**
- toString

in class

NamingException

**Returns:**
- The non-null string representation of this link exception.

---

#### public
String
toString​(boolean detail)

Generates the string representation of this exception.
This string consists of the NamingException information plus
the additional information of resolving the link.
If 'detail' is true, the string also contains information on
the link resolved object. If false, this method is the same
as the form of toString() that accepts no parameters.
This string is used for debugging and not meant to be interpreted
programmatically.

**Overrides:**
- toString

in class

NamingException

**Parameters:**
- detail

- If true, add information about the link resolved
object.

**Returns:**
- The non-null string representation of this link exception.

---

### Additional Sections

#### Class LinkException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LinkException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LinkException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.LinkException

javax.naming.NamingException

- javax.naming.LinkException

javax.naming.LinkException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** LinkLoopException

,

MalformedLinkException

```java
public class
LinkException

extends
NamingException
```

This exception is used to describe problems encountered while resolving links.
Additional information is added to the base NamingException for pinpointing
the problem with the link.

Analogously to how NamingException captures name resolution information,
LinkException captures "link"-name resolution information pinpointing
the problem encountered while resolving a link. All these fields may
be null.

- Link Resolved Name. Portion of link name that has been resolved.

Link Resolved Object. Object to which resolution of link name proceeded.

Link Remaining Name. Portion of link name that has not been resolved.

Link Explanation. Detail explaining why link resolution failed.

A LinkException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single LinkException instance should lock the object.

**Since:** 1.3
**See Also:** Context.lookupLink(javax.naming.Name)

,

LinkRef

,

Serialized Form

public class

LinkException

extends

NamingException

This exception is used to describe problems encountered while resolving links.
Additional information is added to the base NamingException for pinpointing
the problem with the link.

Analogously to how NamingException captures name resolution information,
LinkException captures "link"-name resolution information pinpointing
the problem encountered while resolving a link. All these fields may
be null.

- Link Resolved Name. Portion of link name that has been resolved.

Link Resolved Object. Object to which resolution of link name proceeded.

Link Remaining Name. Portion of link name that has not been resolved.

Link Explanation. Detail explaining why link resolution failed.

A LinkException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single LinkException instance should lock the object.

Analogously to how NamingException captures name resolution information,
LinkException captures "link"-name resolution information pinpointing
the problem encountered while resolving a link. All these fields may
be null.

- Link Resolved Name. Portion of link name that has been resolved.

Link Resolved Object. Object to which resolution of link name proceeded.

Link Remaining Name. Portion of link name that has not been resolved.

Link Explanation. Detail explaining why link resolution failed.

A LinkException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single LinkException instance should lock the object.

Link Resolved Name. Portion of link name that has been resolved.

Link Resolved Object. Object to which resolution of link name proceeded.

Link Remaining Name. Portion of link name that has not been resolved.

Link Explanation. Detail explaining why link resolution failed.

A LinkException instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single LinkException instance should lock the object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

linkExplanation

Contains the exception of why resolution of the link failed.

protected

Name

linkRemainingName

Contains the remaining link name that has not been resolved yet.

protected

Name

linkResolvedName

Contains the part of the link that has been successfully resolved.

protected

Object

linkResolvedObj

Contains the object to which resolution of the part of the link was successful.

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

LinkException

()

Constructs a new instance of LinkException.

LinkException

​(

String

explanation)

Constructs a new instance of LinkException with an explanation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getLinkExplanation

()

Retrieves the explanation associated with the problem encountered
when resolving a link.

Name

getLinkRemainingName

()

Retrieves the remaining unresolved portion of the link name.

Name

getLinkResolvedName

()

Retrieves the leading portion of the link name that was resolved
successfully.

Object

getLinkResolvedObj

()

Retrieves the object to which resolution was successful.

void

setLinkExplanation

​(

String

msg)

Sets the explanation associated with the problem encountered
when resolving a link.

void

setLinkRemainingName

​(

Name

name)

Sets the remaining link name field of this exception.

void

setLinkResolvedName

​(

Name

name)

Sets the resolved link name field of this exception.

void

setLinkResolvedObj

​(

Object

obj)

Sets the link resolved object field of this exception.

String

toString

()

Generates the string representation of this exception.

String

toString

​(boolean detail)

Generates the string representation of this exception.

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

Fields

Modifier and Type

Field

Description

protected

String

linkExplanation

Contains the exception of why resolution of the link failed.

protected

Name

linkRemainingName

Contains the remaining link name that has not been resolved yet.

protected

Name

linkResolvedName

Contains the part of the link that has been successfully resolved.

protected

Object

linkResolvedObj

Contains the object to which resolution of the part of the link was successful.

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

Contains the exception of why resolution of the link failed.

Contains the remaining link name that has not been resolved yet.

Contains the part of the link that has been successfully resolved.

Contains the object to which resolution of the part of the link was successful.

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

LinkException

()

Constructs a new instance of LinkException.

LinkException

​(

String

explanation)

Constructs a new instance of LinkException with an explanation.

---

#### Constructor Summary

Constructs a new instance of LinkException.

Constructs a new instance of LinkException with an explanation.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getLinkExplanation

()

Retrieves the explanation associated with the problem encountered
when resolving a link.

Name

getLinkRemainingName

()

Retrieves the remaining unresolved portion of the link name.

Name

getLinkResolvedName

()

Retrieves the leading portion of the link name that was resolved
successfully.

Object

getLinkResolvedObj

()

Retrieves the object to which resolution was successful.

void

setLinkExplanation

​(

String

msg)

Sets the explanation associated with the problem encountered
when resolving a link.

void

setLinkRemainingName

​(

Name

name)

Sets the remaining link name field of this exception.

void

setLinkResolvedName

​(

Name

name)

Sets the resolved link name field of this exception.

void

setLinkResolvedObj

​(

Object

obj)

Sets the link resolved object field of this exception.

String

toString

()

Generates the string representation of this exception.

String

toString

​(boolean detail)

Generates the string representation of this exception.

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

Retrieves the explanation associated with the problem encountered
when resolving a link.

Retrieves the remaining unresolved portion of the link name.

Retrieves the leading portion of the link name that was resolved
successfully.

Retrieves the object to which resolution was successful.

Sets the explanation associated with the problem encountered
when resolving a link.

Sets the remaining link name field of this exception.

Sets the resolved link name field of this exception.

Sets the link resolved object field of this exception.

Generates the string representation of this exception.

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

============ FIELD DETAIL ===========

- Field Detail

- linkResolvedName

```java
protected
Name
linkResolvedName
```

Contains the part of the link that has been successfully resolved.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkResolvedName()

,

setLinkResolvedName(javax.naming.Name)

- linkResolvedObj

```java
protected
Object
linkResolvedObj
```

Contains the object to which resolution of the part of the link was successful.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkResolvedObj()

,

setLinkResolvedObj(java.lang.Object)

- linkRemainingName

```java
protected
Name
linkRemainingName
```

Contains the remaining link name that has not been resolved yet.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkRemainingName()

,

setLinkRemainingName(javax.naming.Name)

- linkExplanation

```java
protected
String
linkExplanation
```

Contains the exception of why resolution of the link failed.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkExplanation()

,

setLinkExplanation(java.lang.String)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LinkException

```java
public LinkException​(
String
explanation)
```

Constructs a new instance of LinkException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

- LinkException

```java
public LinkException()
```

Constructs a new instance of LinkException.
All the non-link-related and link-related fields are initialized to null.

============ METHOD DETAIL ==========

- Method Detail

- getLinkResolvedName

```java
public
Name
getLinkResolvedName()
```

Retrieves the leading portion of the link name that was resolved
successfully.

**Returns:** The part of the link name that was resolved successfully.
It is a composite name. It can be null, which means
the link resolved name field has not been set.
**See Also:** getLinkResolvedObj()

,

setLinkResolvedName(javax.naming.Name)

- getLinkRemainingName

```java
public
Name
getLinkRemainingName()
```

Retrieves the remaining unresolved portion of the link name.

**Returns:** The part of the link name that has not been resolved.
It is a composite name. It can be null, which means
the link remaining name field has not been set.
**See Also:** setLinkRemainingName(javax.naming.Name)

- getLinkResolvedObj

```java
public
Object
getLinkResolvedObj()
```

Retrieves the object to which resolution was successful.
This is the object to which the resolved link name is bound.

**Returns:** The possibly null object that was resolved so far.
If null, it means the link resolved object field has not been set.
**See Also:** getLinkResolvedName()

,

setLinkResolvedObj(java.lang.Object)

- getLinkExplanation

```java
public
String
getLinkExplanation()
```

Retrieves the explanation associated with the problem encountered
when resolving a link.

**Returns:** The possibly null detail string explaining more about the problem
with resolving a link.
If null, it means there is no
link detail message for this exception.
**See Also:** setLinkExplanation(java.lang.String)

- setLinkExplanation

```java
public void setLinkExplanation​(
String
msg)
```

Sets the explanation associated with the problem encountered
when resolving a link.

**Parameters:** msg

- The possibly null detail string explaining more about the problem
with resolving a link. If null, it means no detail will be recorded.
**See Also:** getLinkExplanation()

- setLinkResolvedName

```java
public void setLinkResolvedName​(
Name
name)
```

Sets the resolved link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

**Parameters:** name

- The name to set resolved link name to. This can be null.
If null, it sets the link resolved name field to null.
**See Also:** getLinkResolvedName()

- setLinkRemainingName

```java
public void setLinkRemainingName​(
Name
name)
```

Sets the remaining link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

**Parameters:** name

- The name to set remaining link name to. This can be null.
If null, it sets the remaining name field to null.
**See Also:** getLinkRemainingName()

- setLinkResolvedObj

```java
public void setLinkResolvedObj​(
Object
obj)
```

Sets the link resolved object field of this exception.
This indicates the last successfully resolved object of link name.

**Parameters:** obj

- The object to set link resolved object to. This can be null.
If null, the link resolved object field is set to null.
**See Also:** getLinkResolvedObj()

- toString

```java
public
String
toString()
```

Generates the string representation of this exception.
This string consists of the NamingException information plus
the link's remaining name.
This string is used for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Returns:** The non-null string representation of this link exception.

- toString

```java
public
String
toString​(boolean detail)
```

Generates the string representation of this exception.
This string consists of the NamingException information plus
the additional information of resolving the link.
If 'detail' is true, the string also contains information on
the link resolved object. If false, this method is the same
as the form of toString() that accepts no parameters.
This string is used for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Parameters:** detail

- If true, add information about the link resolved
object.
**Returns:** The non-null string representation of this link exception.

Field Detail

- linkResolvedName

```java
protected
Name
linkResolvedName
```

Contains the part of the link that has been successfully resolved.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkResolvedName()

,

setLinkResolvedName(javax.naming.Name)

- linkResolvedObj

```java
protected
Object
linkResolvedObj
```

Contains the object to which resolution of the part of the link was successful.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkResolvedObj()

,

setLinkResolvedObj(java.lang.Object)

- linkRemainingName

```java
protected
Name
linkRemainingName
```

Contains the remaining link name that has not been resolved yet.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkRemainingName()

,

setLinkRemainingName(javax.naming.Name)

- linkExplanation

```java
protected
String
linkExplanation
```

Contains the exception of why resolution of the link failed.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkExplanation()

,

setLinkExplanation(java.lang.String)

---

#### Field Detail

linkResolvedName

```java
protected
Name
linkResolvedName
```

Contains the part of the link that has been successfully resolved.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkResolvedName()

,

setLinkResolvedName(javax.naming.Name)

---

#### linkResolvedName

protected

Name

linkResolvedName

Contains the part of the link that has been successfully resolved.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

linkResolvedObj

```java
protected
Object
linkResolvedObj
```

Contains the object to which resolution of the part of the link was successful.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkResolvedObj()

,

setLinkResolvedObj(java.lang.Object)

---

#### linkResolvedObj

protected

Object

linkResolvedObj

Contains the object to which resolution of the part of the link was successful.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

linkRemainingName

```java
protected
Name
linkRemainingName
```

Contains the remaining link name that has not been resolved yet.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkRemainingName()

,

setLinkRemainingName(javax.naming.Name)

---

#### linkRemainingName

protected

Name

linkRemainingName

Contains the remaining link name that has not been resolved yet.
It is a composite name and can be null.
This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

linkExplanation

```java
protected
String
linkExplanation
```

Contains the exception of why resolution of the link failed.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

**See Also:** getLinkExplanation()

,

setLinkExplanation(java.lang.String)

---

#### linkExplanation

protected

String

linkExplanation

Contains the exception of why resolution of the link failed.
Can be null. This field is initialized by the constructors.
You should access and manipulate this field
through its get and set methods.

Constructor Detail

- LinkException

```java
public LinkException​(
String
explanation)
```

Constructs a new instance of LinkException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

- LinkException

```java
public LinkException()
```

Constructs a new instance of LinkException.
All the non-link-related and link-related fields are initialized to null.

---

#### Constructor Detail

LinkException

```java
public LinkException​(
String
explanation)
```

Constructs a new instance of LinkException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

---

#### LinkException

public LinkException​(

String

explanation)

Constructs a new instance of LinkException with an explanation.
All the other fields are initialized to null.

LinkException

```java
public LinkException()
```

Constructs a new instance of LinkException.
All the non-link-related and link-related fields are initialized to null.

---

#### LinkException

public LinkException()

Constructs a new instance of LinkException.
All the non-link-related and link-related fields are initialized to null.

Method Detail

- getLinkResolvedName

```java
public
Name
getLinkResolvedName()
```

Retrieves the leading portion of the link name that was resolved
successfully.

**Returns:** The part of the link name that was resolved successfully.
It is a composite name. It can be null, which means
the link resolved name field has not been set.
**See Also:** getLinkResolvedObj()

,

setLinkResolvedName(javax.naming.Name)

- getLinkRemainingName

```java
public
Name
getLinkRemainingName()
```

Retrieves the remaining unresolved portion of the link name.

**Returns:** The part of the link name that has not been resolved.
It is a composite name. It can be null, which means
the link remaining name field has not been set.
**See Also:** setLinkRemainingName(javax.naming.Name)

- getLinkResolvedObj

```java
public
Object
getLinkResolvedObj()
```

Retrieves the object to which resolution was successful.
This is the object to which the resolved link name is bound.

**Returns:** The possibly null object that was resolved so far.
If null, it means the link resolved object field has not been set.
**See Also:** getLinkResolvedName()

,

setLinkResolvedObj(java.lang.Object)

- getLinkExplanation

```java
public
String
getLinkExplanation()
```

Retrieves the explanation associated with the problem encountered
when resolving a link.

**Returns:** The possibly null detail string explaining more about the problem
with resolving a link.
If null, it means there is no
link detail message for this exception.
**See Also:** setLinkExplanation(java.lang.String)

- setLinkExplanation

```java
public void setLinkExplanation​(
String
msg)
```

Sets the explanation associated with the problem encountered
when resolving a link.

**Parameters:** msg

- The possibly null detail string explaining more about the problem
with resolving a link. If null, it means no detail will be recorded.
**See Also:** getLinkExplanation()

- setLinkResolvedName

```java
public void setLinkResolvedName​(
Name
name)
```

Sets the resolved link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

**Parameters:** name

- The name to set resolved link name to. This can be null.
If null, it sets the link resolved name field to null.
**See Also:** getLinkResolvedName()

- setLinkRemainingName

```java
public void setLinkRemainingName​(
Name
name)
```

Sets the remaining link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

**Parameters:** name

- The name to set remaining link name to. This can be null.
If null, it sets the remaining name field to null.
**See Also:** getLinkRemainingName()

- setLinkResolvedObj

```java
public void setLinkResolvedObj​(
Object
obj)
```

Sets the link resolved object field of this exception.
This indicates the last successfully resolved object of link name.

**Parameters:** obj

- The object to set link resolved object to. This can be null.
If null, the link resolved object field is set to null.
**See Also:** getLinkResolvedObj()

- toString

```java
public
String
toString()
```

Generates the string representation of this exception.
This string consists of the NamingException information plus
the link's remaining name.
This string is used for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Returns:** The non-null string representation of this link exception.

- toString

```java
public
String
toString​(boolean detail)
```

Generates the string representation of this exception.
This string consists of the NamingException information plus
the additional information of resolving the link.
If 'detail' is true, the string also contains information on
the link resolved object. If false, this method is the same
as the form of toString() that accepts no parameters.
This string is used for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Parameters:** detail

- If true, add information about the link resolved
object.
**Returns:** The non-null string representation of this link exception.

---

#### Method Detail

getLinkResolvedName

```java
public
Name
getLinkResolvedName()
```

Retrieves the leading portion of the link name that was resolved
successfully.

**Returns:** The part of the link name that was resolved successfully.
It is a composite name. It can be null, which means
the link resolved name field has not been set.
**See Also:** getLinkResolvedObj()

,

setLinkResolvedName(javax.naming.Name)

---

#### getLinkResolvedName

public

Name

getLinkResolvedName()

Retrieves the leading portion of the link name that was resolved
successfully.

getLinkRemainingName

```java
public
Name
getLinkRemainingName()
```

Retrieves the remaining unresolved portion of the link name.

**Returns:** The part of the link name that has not been resolved.
It is a composite name. It can be null, which means
the link remaining name field has not been set.
**See Also:** setLinkRemainingName(javax.naming.Name)

---

#### getLinkRemainingName

public

Name

getLinkRemainingName()

Retrieves the remaining unresolved portion of the link name.

getLinkResolvedObj

```java
public
Object
getLinkResolvedObj()
```

Retrieves the object to which resolution was successful.
This is the object to which the resolved link name is bound.

**Returns:** The possibly null object that was resolved so far.
If null, it means the link resolved object field has not been set.
**See Also:** getLinkResolvedName()

,

setLinkResolvedObj(java.lang.Object)

---

#### getLinkResolvedObj

public

Object

getLinkResolvedObj()

Retrieves the object to which resolution was successful.
This is the object to which the resolved link name is bound.

getLinkExplanation

```java
public
String
getLinkExplanation()
```

Retrieves the explanation associated with the problem encountered
when resolving a link.

**Returns:** The possibly null detail string explaining more about the problem
with resolving a link.
If null, it means there is no
link detail message for this exception.
**See Also:** setLinkExplanation(java.lang.String)

---

#### getLinkExplanation

public

String

getLinkExplanation()

Retrieves the explanation associated with the problem encountered
when resolving a link.

setLinkExplanation

```java
public void setLinkExplanation​(
String
msg)
```

Sets the explanation associated with the problem encountered
when resolving a link.

**Parameters:** msg

- The possibly null detail string explaining more about the problem
with resolving a link. If null, it means no detail will be recorded.
**See Also:** getLinkExplanation()

---

#### setLinkExplanation

public void setLinkExplanation​(

String

msg)

Sets the explanation associated with the problem encountered
when resolving a link.

setLinkResolvedName

```java
public void setLinkResolvedName​(
Name
name)
```

Sets the resolved link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

**Parameters:** name

- The name to set resolved link name to. This can be null.
If null, it sets the link resolved name field to null.
**See Also:** getLinkResolvedName()

---

#### setLinkResolvedName

public void setLinkResolvedName​(

Name

name)

Sets the resolved link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

setLinkRemainingName

```java
public void setLinkRemainingName​(
Name
name)
```

Sets the remaining link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

**Parameters:** name

- The name to set remaining link name to. This can be null.
If null, it sets the remaining name field to null.
**See Also:** getLinkRemainingName()

---

#### setLinkRemainingName

public void setLinkRemainingName​(

Name

name)

Sets the remaining link name field of this exception.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

name

is a composite name. If the intent is to set
this field using a compound name or string, you must
"stringify" the compound name, and create a composite
name with a single component using the string. You can then
invoke this method using the resulting composite name.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

A copy of

name

is made and stored.
Subsequent changes to

name

do not
affect the copy in this NamingException and vice versa.

setLinkResolvedObj

```java
public void setLinkResolvedObj​(
Object
obj)
```

Sets the link resolved object field of this exception.
This indicates the last successfully resolved object of link name.

**Parameters:** obj

- The object to set link resolved object to. This can be null.
If null, the link resolved object field is set to null.
**See Also:** getLinkResolvedObj()

---

#### setLinkResolvedObj

public void setLinkResolvedObj​(

Object

obj)

Sets the link resolved object field of this exception.
This indicates the last successfully resolved object of link name.

toString

```java
public
String
toString()
```

Generates the string representation of this exception.
This string consists of the NamingException information plus
the link's remaining name.
This string is used for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Returns:** The non-null string representation of this link exception.

---

#### toString

public

String

toString()

Generates the string representation of this exception.
This string consists of the NamingException information plus
the link's remaining name.
This string is used for debugging and not meant to be interpreted
programmatically.

toString

```java
public
String
toString​(boolean detail)
```

Generates the string representation of this exception.
This string consists of the NamingException information plus
the additional information of resolving the link.
If 'detail' is true, the string also contains information on
the link resolved object. If false, this method is the same
as the form of toString() that accepts no parameters.
This string is used for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

NamingException
**Parameters:** detail

- If true, add information about the link resolved
object.
**Returns:** The non-null string representation of this link exception.

---

#### toString

public

String

toString​(boolean detail)

Generates the string representation of this exception.
This string consists of the NamingException information plus
the additional information of resolving the link.
If 'detail' is true, the string also contains information on
the link resolved object. If false, this method is the same
as the form of toString() that accepts no parameters.
This string is used for debugging and not meant to be interpreted
programmatically.

---


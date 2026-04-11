# Class GSSUtil

**Source:** `jdk.security.jgss\com\sun\security\jgss\GSSUtil.html`

### Class Description

```java
public class
GSSUtil

extends
Object
```

GSS-API Utilities for using in conjunction with Sun Microsystem's
implementation of Java GSS-API.

---

### Field Details

*No entries found.*

### Constructor Details

#### public GSSUtil()

*No description found.*

---

### Method Details

#### public static
Subject
createSubject​(
GSSName
principals,

GSSCredential
credentials)

Use this method to convert a GSSName and GSSCredential into a
Subject. Typically this would be done by a server that wants to
impersonate a client thread at the Java level by setting a client
Subject in the current access control context. If the server is merely
interested in using a principal based policy in its local JVM, then
it only needs to provide the GSSName of the client.

The elements from the GSSName are placed in the principals set of this
Subject and those from the GSSCredential are placed in the private
credentials set of the Subject. Any Kerberos specific elements that
are added to the subject will be instances of the standard Kerberos
implementation classes defined in javax.security.auth.kerberos.

**Parameters:**
- principals

- a GSSName containing one or more mechanism specific
representations of the same entity. These mechanism specific
representations will be populated in the returned Subject's principal
set.
- credentials

- a GSSCredential containing one or more mechanism
specific credentials for the same entity. These mechanism specific
credentials will be populated in the returned Subject's private
credential set. Passing in a value of null will imply that the private
credential set should be left empty.

**Returns:**
- a Subject with the entries that contain elements from the
given GSSName and GSSCredential.

---

### Additional Sections

#### Class GSSUtil

java.lang.Object

- com.sun.security.jgss.GSSUtil

com.sun.security.jgss.GSSUtil

```java
public class
GSSUtil

extends
Object
```

GSS-API Utilities for using in conjunction with Sun Microsystem's
implementation of Java GSS-API.

public class

GSSUtil

extends

Object

GSS-API Utilities for using in conjunction with Sun Microsystem's
implementation of Java GSS-API.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GSSUtil

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Subject

createSubject

​(

GSSName

principals,

GSSCredential

credentials)

Use this method to convert a GSSName and GSSCredential into a
Subject.

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

Constructor Summary

Constructors

Constructor

Description

GSSUtil

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Subject

createSubject

​(

GSSName

principals,

GSSCredential

credentials)

Use this method to convert a GSSName and GSSCredential into a
Subject.

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

Use this method to convert a GSSName and GSSCredential into a
Subject.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GSSUtil

```java
public GSSUtil()
```

============ METHOD DETAIL ==========

- Method Detail

- createSubject

```java
public static
Subject
createSubject​(
GSSName
principals,

GSSCredential
credentials)
```

Use this method to convert a GSSName and GSSCredential into a
Subject. Typically this would be done by a server that wants to
impersonate a client thread at the Java level by setting a client
Subject in the current access control context. If the server is merely
interested in using a principal based policy in its local JVM, then
it only needs to provide the GSSName of the client.

The elements from the GSSName are placed in the principals set of this
Subject and those from the GSSCredential are placed in the private
credentials set of the Subject. Any Kerberos specific elements that
are added to the subject will be instances of the standard Kerberos
implementation classes defined in javax.security.auth.kerberos.

**Parameters:** principals

- a GSSName containing one or more mechanism specific
representations of the same entity. These mechanism specific
representations will be populated in the returned Subject's principal
set.
**Parameters:** credentials

- a GSSCredential containing one or more mechanism
specific credentials for the same entity. These mechanism specific
credentials will be populated in the returned Subject's private
credential set. Passing in a value of null will imply that the private
credential set should be left empty.
**Returns:** a Subject with the entries that contain elements from the
given GSSName and GSSCredential.

Constructor Detail

- GSSUtil

```java
public GSSUtil()
```

---

#### Constructor Detail

GSSUtil

```java
public GSSUtil()
```

---

#### GSSUtil

public GSSUtil()

Method Detail

- createSubject

```java
public static
Subject
createSubject​(
GSSName
principals,

GSSCredential
credentials)
```

Use this method to convert a GSSName and GSSCredential into a
Subject. Typically this would be done by a server that wants to
impersonate a client thread at the Java level by setting a client
Subject in the current access control context. If the server is merely
interested in using a principal based policy in its local JVM, then
it only needs to provide the GSSName of the client.

The elements from the GSSName are placed in the principals set of this
Subject and those from the GSSCredential are placed in the private
credentials set of the Subject. Any Kerberos specific elements that
are added to the subject will be instances of the standard Kerberos
implementation classes defined in javax.security.auth.kerberos.

**Parameters:** principals

- a GSSName containing one or more mechanism specific
representations of the same entity. These mechanism specific
representations will be populated in the returned Subject's principal
set.
**Parameters:** credentials

- a GSSCredential containing one or more mechanism
specific credentials for the same entity. These mechanism specific
credentials will be populated in the returned Subject's private
credential set. Passing in a value of null will imply that the private
credential set should be left empty.
**Returns:** a Subject with the entries that contain elements from the
given GSSName and GSSCredential.

---

#### Method Detail

createSubject

```java
public static
Subject
createSubject​(
GSSName
principals,

GSSCredential
credentials)
```

Use this method to convert a GSSName and GSSCredential into a
Subject. Typically this would be done by a server that wants to
impersonate a client thread at the Java level by setting a client
Subject in the current access control context. If the server is merely
interested in using a principal based policy in its local JVM, then
it only needs to provide the GSSName of the client.

The elements from the GSSName are placed in the principals set of this
Subject and those from the GSSCredential are placed in the private
credentials set of the Subject. Any Kerberos specific elements that
are added to the subject will be instances of the standard Kerberos
implementation classes defined in javax.security.auth.kerberos.

**Parameters:** principals

- a GSSName containing one or more mechanism specific
representations of the same entity. These mechanism specific
representations will be populated in the returned Subject's principal
set.
**Parameters:** credentials

- a GSSCredential containing one or more mechanism
specific credentials for the same entity. These mechanism specific
credentials will be populated in the returned Subject's private
credential set. Passing in a value of null will imply that the private
credential set should be left empty.
**Returns:** a Subject with the entries that contain elements from the
given GSSName and GSSCredential.

---

#### createSubject

public static

Subject

createSubject​(

GSSName

principals,

GSSCredential

credentials)

Use this method to convert a GSSName and GSSCredential into a
Subject. Typically this would be done by a server that wants to
impersonate a client thread at the Java level by setting a client
Subject in the current access control context. If the server is merely
interested in using a principal based policy in its local JVM, then
it only needs to provide the GSSName of the client.

The elements from the GSSName are placed in the principals set of this
Subject and those from the GSSCredential are placed in the private
credentials set of the Subject. Any Kerberos specific elements that
are added to the subject will be instances of the standard Kerberos
implementation classes defined in javax.security.auth.kerberos.

---


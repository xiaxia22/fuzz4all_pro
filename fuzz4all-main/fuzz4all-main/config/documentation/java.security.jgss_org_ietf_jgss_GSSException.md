# Class GSSException

**Source:** `java.security.jgss\org\ietf\jgss\GSSException.html`

### Class Description

```java
public class
GSSException

extends
Exception
```

This exception is thrown whenever a GSS-API error occurs, including
any mechanism specific error. It may contain both the major and the
minor GSS-API status codes. Major error codes are those defined at the
GSS-API level in this class. Minor error codes are mechanism specific
error codes that can provide additional information. The underlying
mechanism implementation is responsible for setting appropriate minor
status codes when throwing this exception. Aside from delivering the
numeric error codes to the caller, this class performs the mapping from
their numeric values to textual representations.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int BAD_BINDINGS

Channel bindings mismatch.

**See Also:**
- Constant Field Values

---

#### public static final int BAD_MECH

Unsupported mechanism requested.

**See Also:**
- Constant Field Values

---

#### public static final int BAD_NAME

Invalid name provided.

**See Also:**
- Constant Field Values

---

#### public static final int BAD_NAMETYPE

Name of unsupported type provided.

**See Also:**
- Constant Field Values

---

#### public static final int BAD_STATUS

Invalid status code.

**See Also:**
- Constant Field Values

---

#### public static final int BAD_MIC

Token had invalid integrity check.

**See Also:**
- Constant Field Values

---

#### public static final int CONTEXT_EXPIRED

Security context expired.

**See Also:**
- Constant Field Values

---

#### public static final int CREDENTIALS_EXPIRED

Expired credentials.

**See Also:**
- Constant Field Values

---

#### public static final int DEFECTIVE_CREDENTIAL

Defective credentials.

**See Also:**
- Constant Field Values

---

#### public static final int DEFECTIVE_TOKEN

Defective token.

**See Also:**
- Constant Field Values

---

#### public static final int FAILURE

General failure, unspecified at GSS-API level.

**See Also:**
- Constant Field Values

---

#### public static final int NO_CONTEXT

Invalid security context.

**See Also:**
- Constant Field Values

---

#### public static final int NO_CRED

Invalid credentials.

**See Also:**
- Constant Field Values

---

#### public static final int BAD_QOP

Unsupported QOP value.

**See Also:**
- Constant Field Values

---

#### public static final int UNAUTHORIZED

Operation unauthorized.

**See Also:**
- Constant Field Values

---

#### public static final int UNAVAILABLE

Operation unavailable.

**See Also:**
- Constant Field Values

---

#### public static final int DUPLICATE_ELEMENT

Duplicate credential element requested.

**See Also:**
- Constant Field Values

---

#### public static final int NAME_NOT_MN

Name contains multi-mechanism elements.

**See Also:**
- Constant Field Values

---

#### public static final int DUPLICATE_TOKEN

The token was a duplicate of an earlier token.
This is a fatal error code that may occur during
context establishment. It is not used to indicate
supplementary status values. The MessageProp object is
used for that purpose.

**See Also:**
- Constant Field Values

---

#### public static final int OLD_TOKEN

The token's validity period has expired. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:**
- Constant Field Values

---

#### public static final int UNSEQ_TOKEN

A later token has already been processed. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:**
- Constant Field Values

---

#### public static final int GAP_TOKEN

An expected per-message token was not received. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public GSSException​(int majorCode)

Creates a GSSException object with a specified major code.

**Parameters:**
- majorCode

- the The GSS error code for the problem causing this
exception to be thrown.

---

#### public GSSException​(int majorCode,
int minorCode,

String
minorString)

Creates a GSSException object with the specified major code, minor
code, and minor code textual explanation. This constructor is to be
used when the exception is originating from the underlying mechanism
level. It allows the setting of both the GSS code and the mechanism
code.

**Parameters:**
- majorCode

- the GSS error code for the problem causing this
exception to be thrown.
- minorCode

- the mechanism level error code for the problem
causing this exception to be thrown.
- minorString

- the textual explanation of the mechanism error
code.

---

### Method Details

#### public int getMajor()

Returns the GSS-API level major error code for the problem causing
this exception to be thrown. Major error codes are
defined at the mechanism independent GSS-API level in this
class. Mechanism specific error codes that might provide more
information are set as the minor error code.

**Returns:**
- int the GSS-API level major error code causing this exception

**See Also:**
- getMajorString()

,

getMinor()

,

getMinorString()

---

#### public int getMinor()

Returns the mechanism level error code for the problem causing this
exception to be thrown. The minor code is set by the underlying
mechanism.

**Returns:**
- int the mechanism error code; 0 indicates that it has not
been set.

**See Also:**
- getMinorString()

,

setMinor(int, java.lang.String)

---

#### public
String
getMajorString()

Returns a string explaining the GSS-API level major error code in
this exception.

**Returns:**
- String explanation string for the major error code

**See Also:**
- getMajor()

,

toString()

---

#### public
String
getMinorString()

Returns a string explaining the mechanism specific error code.
If the minor status code is 0, then no mechanism level error details
will be available.

**Returns:**
- String a textual explanation of mechanism error code

**See Also:**
- getMinor()

,

getMajorString()

,

toString()

---

#### public void setMinor​(int minorCode,

String
message)

Used by the exception thrower to set the mechanism
level minor error code and its string explanation. This is used by
mechanism providers to indicate error details.

**Parameters:**
- minorCode

- the mechanism specific error code
- message

- textual explanation of the mechanism error code

**See Also:**
- getMinor()

---

#### public
String
toString()

Returns a textual representation of both the major and the minor
status codes.

**Overrides:**
- toString

in class

Throwable

**Returns:**
- a String with the error descriptions

---

#### public
String
getMessage()

Returns a textual representation of both the major and the minor
status codes.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- a String with the error descriptions

---

### Additional Sections

#### Class GSSException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - org.ietf.jgss.GSSException

java.lang.Throwable

- java.lang.Exception
- - org.ietf.jgss.GSSException

java.lang.Exception

- org.ietf.jgss.GSSException

org.ietf.jgss.GSSException

**All Implemented Interfaces:** Serializable

```java
public class
GSSException

extends
Exception
```

This exception is thrown whenever a GSS-API error occurs, including
any mechanism specific error. It may contain both the major and the
minor GSS-API status codes. Major error codes are those defined at the
GSS-API level in this class. Minor error codes are mechanism specific
error codes that can provide additional information. The underlying
mechanism implementation is responsible for setting appropriate minor
status codes when throwing this exception. Aside from delivering the
numeric error codes to the caller, this class performs the mapping from
their numeric values to textual representations.

**Since:** 1.4
**See Also:** Serialized Form

public class

GSSException

extends

Exception

This exception is thrown whenever a GSS-API error occurs, including
any mechanism specific error. It may contain both the major and the
minor GSS-API status codes. Major error codes are those defined at the
GSS-API level in this class. Minor error codes are mechanism specific
error codes that can provide additional information. The underlying
mechanism implementation is responsible for setting appropriate minor
status codes when throwing this exception. Aside from delivering the
numeric error codes to the caller, this class performs the mapping from
their numeric values to textual representations.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

BAD_BINDINGS

Channel bindings mismatch.

static int

BAD_MECH

Unsupported mechanism requested.

static int

BAD_MIC

Token had invalid integrity check.

static int

BAD_NAME

Invalid name provided.

static int

BAD_NAMETYPE

Name of unsupported type provided.

static int

BAD_QOP

Unsupported QOP value.

static int

BAD_STATUS

Invalid status code.

static int

CONTEXT_EXPIRED

Security context expired.

static int

CREDENTIALS_EXPIRED

Expired credentials.

static int

DEFECTIVE_CREDENTIAL

Defective credentials.

static int

DEFECTIVE_TOKEN

Defective token.

static int

DUPLICATE_ELEMENT

Duplicate credential element requested.

static int

DUPLICATE_TOKEN

The token was a duplicate of an earlier token.

static int

FAILURE

General failure, unspecified at GSS-API level.

static int

GAP_TOKEN

An expected per-message token was not received.

static int

NAME_NOT_MN

Name contains multi-mechanism elements.

static int

NO_CONTEXT

Invalid security context.

static int

NO_CRED

Invalid credentials.

static int

OLD_TOKEN

The token's validity period has expired.

static int

UNAUTHORIZED

Operation unauthorized.

static int

UNAVAILABLE

Operation unavailable.

static int

UNSEQ_TOKEN

A later token has already been processed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GSSException

​(int majorCode)

Creates a GSSException object with a specified major code.

GSSException

​(int majorCode,
int minorCode,

String

minorString)

Creates a GSSException object with the specified major code, minor
code, and minor code textual explanation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getMajor

()

Returns the GSS-API level major error code for the problem causing
this exception to be thrown.

String

getMajorString

()

Returns a string explaining the GSS-API level major error code in
this exception.

String

getMessage

()

Returns a textual representation of both the major and the minor
status codes.

int

getMinor

()

Returns the mechanism level error code for the problem causing this
exception to be thrown.

String

getMinorString

()

Returns a string explaining the mechanism specific error code.

void

setMinor

​(int minorCode,

String

message)

Used by the exception thrower to set the mechanism
level minor error code and its string explanation.

String

toString

()

Returns a textual representation of both the major and the minor
status codes.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getStackTrace

,

getSuppressed

,

initCause

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

static int

BAD_BINDINGS

Channel bindings mismatch.

static int

BAD_MECH

Unsupported mechanism requested.

static int

BAD_MIC

Token had invalid integrity check.

static int

BAD_NAME

Invalid name provided.

static int

BAD_NAMETYPE

Name of unsupported type provided.

static int

BAD_QOP

Unsupported QOP value.

static int

BAD_STATUS

Invalid status code.

static int

CONTEXT_EXPIRED

Security context expired.

static int

CREDENTIALS_EXPIRED

Expired credentials.

static int

DEFECTIVE_CREDENTIAL

Defective credentials.

static int

DEFECTIVE_TOKEN

Defective token.

static int

DUPLICATE_ELEMENT

Duplicate credential element requested.

static int

DUPLICATE_TOKEN

The token was a duplicate of an earlier token.

static int

FAILURE

General failure, unspecified at GSS-API level.

static int

GAP_TOKEN

An expected per-message token was not received.

static int

NAME_NOT_MN

Name contains multi-mechanism elements.

static int

NO_CONTEXT

Invalid security context.

static int

NO_CRED

Invalid credentials.

static int

OLD_TOKEN

The token's validity period has expired.

static int

UNAUTHORIZED

Operation unauthorized.

static int

UNAVAILABLE

Operation unavailable.

static int

UNSEQ_TOKEN

A later token has already been processed.

---

#### Field Summary

Channel bindings mismatch.

Unsupported mechanism requested.

Token had invalid integrity check.

Invalid name provided.

Name of unsupported type provided.

Unsupported QOP value.

Invalid status code.

Security context expired.

Expired credentials.

Defective credentials.

Defective token.

Duplicate credential element requested.

The token was a duplicate of an earlier token.

General failure, unspecified at GSS-API level.

An expected per-message token was not received.

Name contains multi-mechanism elements.

Invalid security context.

Invalid credentials.

The token's validity period has expired.

Operation unauthorized.

Operation unavailable.

A later token has already been processed.

Constructor Summary

Constructors

Constructor

Description

GSSException

​(int majorCode)

Creates a GSSException object with a specified major code.

GSSException

​(int majorCode,
int minorCode,

String

minorString)

Creates a GSSException object with the specified major code, minor
code, and minor code textual explanation.

---

#### Constructor Summary

Creates a GSSException object with a specified major code.

Creates a GSSException object with the specified major code, minor
code, and minor code textual explanation.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getMajor

()

Returns the GSS-API level major error code for the problem causing
this exception to be thrown.

String

getMajorString

()

Returns a string explaining the GSS-API level major error code in
this exception.

String

getMessage

()

Returns a textual representation of both the major and the minor
status codes.

int

getMinor

()

Returns the mechanism level error code for the problem causing this
exception to be thrown.

String

getMinorString

()

Returns a string explaining the mechanism specific error code.

void

setMinor

​(int minorCode,

String

message)

Used by the exception thrower to set the mechanism
level minor error code and its string explanation.

String

toString

()

Returns a textual representation of both the major and the minor
status codes.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getStackTrace

,

getSuppressed

,

initCause

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

Returns the GSS-API level major error code for the problem causing
this exception to be thrown.

Returns a string explaining the GSS-API level major error code in
this exception.

Returns a textual representation of both the major and the minor
status codes.

Returns the mechanism level error code for the problem causing this
exception to be thrown.

Returns a string explaining the mechanism specific error code.

Used by the exception thrower to set the mechanism
level minor error code and its string explanation.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getStackTrace

,

getSuppressed

,

initCause

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

- BAD_BINDINGS

```java
public static final int BAD_BINDINGS
```

Channel bindings mismatch.

**See Also:** Constant Field Values

- BAD_MECH

```java
public static final int BAD_MECH
```

Unsupported mechanism requested.

**See Also:** Constant Field Values

- BAD_NAME

```java
public static final int BAD_NAME
```

Invalid name provided.

**See Also:** Constant Field Values

- BAD_NAMETYPE

```java
public static final int BAD_NAMETYPE
```

Name of unsupported type provided.

**See Also:** Constant Field Values

- BAD_STATUS

```java
public static final int BAD_STATUS
```

Invalid status code.

**See Also:** Constant Field Values

- BAD_MIC

```java
public static final int BAD_MIC
```

Token had invalid integrity check.

**See Also:** Constant Field Values

- CONTEXT_EXPIRED

```java
public static final int CONTEXT_EXPIRED
```

Security context expired.

**See Also:** Constant Field Values

- CREDENTIALS_EXPIRED

```java
public static final int CREDENTIALS_EXPIRED
```

Expired credentials.

**See Also:** Constant Field Values

- DEFECTIVE_CREDENTIAL

```java
public static final int DEFECTIVE_CREDENTIAL
```

Defective credentials.

**See Also:** Constant Field Values

- DEFECTIVE_TOKEN

```java
public static final int DEFECTIVE_TOKEN
```

Defective token.

**See Also:** Constant Field Values

- FAILURE

```java
public static final int FAILURE
```

General failure, unspecified at GSS-API level.

**See Also:** Constant Field Values

- NO_CONTEXT

```java
public static final int NO_CONTEXT
```

Invalid security context.

**See Also:** Constant Field Values

- NO_CRED

```java
public static final int NO_CRED
```

Invalid credentials.

**See Also:** Constant Field Values

- BAD_QOP

```java
public static final int BAD_QOP
```

Unsupported QOP value.

**See Also:** Constant Field Values

- UNAUTHORIZED

```java
public static final int UNAUTHORIZED
```

Operation unauthorized.

**See Also:** Constant Field Values

- UNAVAILABLE

```java
public static final int UNAVAILABLE
```

Operation unavailable.

**See Also:** Constant Field Values

- DUPLICATE_ELEMENT

```java
public static final int DUPLICATE_ELEMENT
```

Duplicate credential element requested.

**See Also:** Constant Field Values

- NAME_NOT_MN

```java
public static final int NAME_NOT_MN
```

Name contains multi-mechanism elements.

**See Also:** Constant Field Values

- DUPLICATE_TOKEN

```java
public static final int DUPLICATE_TOKEN
```

The token was a duplicate of an earlier token.
This is a fatal error code that may occur during
context establishment. It is not used to indicate
supplementary status values. The MessageProp object is
used for that purpose.

**See Also:** Constant Field Values

- OLD_TOKEN

```java
public static final int OLD_TOKEN
```

The token's validity period has expired. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

- UNSEQ_TOKEN

```java
public static final int UNSEQ_TOKEN
```

A later token has already been processed. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

- GAP_TOKEN

```java
public static final int GAP_TOKEN
```

An expected per-message token was not received. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GSSException

```java
public GSSException​(int majorCode)
```

Creates a GSSException object with a specified major code.

**Parameters:** majorCode

- the The GSS error code for the problem causing this
exception to be thrown.

- GSSException

```java
public GSSException​(int majorCode,
int minorCode,

String
minorString)
```

Creates a GSSException object with the specified major code, minor
code, and minor code textual explanation. This constructor is to be
used when the exception is originating from the underlying mechanism
level. It allows the setting of both the GSS code and the mechanism
code.

**Parameters:** majorCode

- the GSS error code for the problem causing this
exception to be thrown.
**Parameters:** minorCode

- the mechanism level error code for the problem
causing this exception to be thrown.
**Parameters:** minorString

- the textual explanation of the mechanism error
code.

============ METHOD DETAIL ==========

- Method Detail

- getMajor

```java
public int getMajor()
```

Returns the GSS-API level major error code for the problem causing
this exception to be thrown. Major error codes are
defined at the mechanism independent GSS-API level in this
class. Mechanism specific error codes that might provide more
information are set as the minor error code.

**Returns:** int the GSS-API level major error code causing this exception
**See Also:** getMajorString()

,

getMinor()

,

getMinorString()

- getMinor

```java
public int getMinor()
```

Returns the mechanism level error code for the problem causing this
exception to be thrown. The minor code is set by the underlying
mechanism.

**Returns:** int the mechanism error code; 0 indicates that it has not
been set.
**See Also:** getMinorString()

,

setMinor(int, java.lang.String)

- getMajorString

```java
public
String
getMajorString()
```

Returns a string explaining the GSS-API level major error code in
this exception.

**Returns:** String explanation string for the major error code
**See Also:** getMajor()

,

toString()

- getMinorString

```java
public
String
getMinorString()
```

Returns a string explaining the mechanism specific error code.
If the minor status code is 0, then no mechanism level error details
will be available.

**Returns:** String a textual explanation of mechanism error code
**See Also:** getMinor()

,

getMajorString()

,

toString()

- setMinor

```java
public void setMinor​(int minorCode,

String
message)
```

Used by the exception thrower to set the mechanism
level minor error code and its string explanation. This is used by
mechanism providers to indicate error details.

**Parameters:** minorCode

- the mechanism specific error code
**Parameters:** message

- textual explanation of the mechanism error code
**See Also:** getMinor()

- toString

```java
public
String
toString()
```

Returns a textual representation of both the major and the minor
status codes.

**Overrides:** toString

in class

Throwable
**Returns:** a String with the error descriptions

- getMessage

```java
public
String
getMessage()
```

Returns a textual representation of both the major and the minor
status codes.

**Overrides:** getMessage

in class

Throwable
**Returns:** a String with the error descriptions

Field Detail

- BAD_BINDINGS

```java
public static final int BAD_BINDINGS
```

Channel bindings mismatch.

**See Also:** Constant Field Values

- BAD_MECH

```java
public static final int BAD_MECH
```

Unsupported mechanism requested.

**See Also:** Constant Field Values

- BAD_NAME

```java
public static final int BAD_NAME
```

Invalid name provided.

**See Also:** Constant Field Values

- BAD_NAMETYPE

```java
public static final int BAD_NAMETYPE
```

Name of unsupported type provided.

**See Also:** Constant Field Values

- BAD_STATUS

```java
public static final int BAD_STATUS
```

Invalid status code.

**See Also:** Constant Field Values

- BAD_MIC

```java
public static final int BAD_MIC
```

Token had invalid integrity check.

**See Also:** Constant Field Values

- CONTEXT_EXPIRED

```java
public static final int CONTEXT_EXPIRED
```

Security context expired.

**See Also:** Constant Field Values

- CREDENTIALS_EXPIRED

```java
public static final int CREDENTIALS_EXPIRED
```

Expired credentials.

**See Also:** Constant Field Values

- DEFECTIVE_CREDENTIAL

```java
public static final int DEFECTIVE_CREDENTIAL
```

Defective credentials.

**See Also:** Constant Field Values

- DEFECTIVE_TOKEN

```java
public static final int DEFECTIVE_TOKEN
```

Defective token.

**See Also:** Constant Field Values

- FAILURE

```java
public static final int FAILURE
```

General failure, unspecified at GSS-API level.

**See Also:** Constant Field Values

- NO_CONTEXT

```java
public static final int NO_CONTEXT
```

Invalid security context.

**See Also:** Constant Field Values

- NO_CRED

```java
public static final int NO_CRED
```

Invalid credentials.

**See Also:** Constant Field Values

- BAD_QOP

```java
public static final int BAD_QOP
```

Unsupported QOP value.

**See Also:** Constant Field Values

- UNAUTHORIZED

```java
public static final int UNAUTHORIZED
```

Operation unauthorized.

**See Also:** Constant Field Values

- UNAVAILABLE

```java
public static final int UNAVAILABLE
```

Operation unavailable.

**See Also:** Constant Field Values

- DUPLICATE_ELEMENT

```java
public static final int DUPLICATE_ELEMENT
```

Duplicate credential element requested.

**See Also:** Constant Field Values

- NAME_NOT_MN

```java
public static final int NAME_NOT_MN
```

Name contains multi-mechanism elements.

**See Also:** Constant Field Values

- DUPLICATE_TOKEN

```java
public static final int DUPLICATE_TOKEN
```

The token was a duplicate of an earlier token.
This is a fatal error code that may occur during
context establishment. It is not used to indicate
supplementary status values. The MessageProp object is
used for that purpose.

**See Also:** Constant Field Values

- OLD_TOKEN

```java
public static final int OLD_TOKEN
```

The token's validity period has expired. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

- UNSEQ_TOKEN

```java
public static final int UNSEQ_TOKEN
```

A later token has already been processed. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

- GAP_TOKEN

```java
public static final int GAP_TOKEN
```

An expected per-message token was not received. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

---

#### Field Detail

BAD_BINDINGS

```java
public static final int BAD_BINDINGS
```

Channel bindings mismatch.

**See Also:** Constant Field Values

---

#### BAD_BINDINGS

public static final int BAD_BINDINGS

Channel bindings mismatch.

BAD_MECH

```java
public static final int BAD_MECH
```

Unsupported mechanism requested.

**See Also:** Constant Field Values

---

#### BAD_MECH

public static final int BAD_MECH

Unsupported mechanism requested.

BAD_NAME

```java
public static final int BAD_NAME
```

Invalid name provided.

**See Also:** Constant Field Values

---

#### BAD_NAME

public static final int BAD_NAME

Invalid name provided.

BAD_NAMETYPE

```java
public static final int BAD_NAMETYPE
```

Name of unsupported type provided.

**See Also:** Constant Field Values

---

#### BAD_NAMETYPE

public static final int BAD_NAMETYPE

Name of unsupported type provided.

BAD_STATUS

```java
public static final int BAD_STATUS
```

Invalid status code.

**See Also:** Constant Field Values

---

#### BAD_STATUS

public static final int BAD_STATUS

Invalid status code.

BAD_MIC

```java
public static final int BAD_MIC
```

Token had invalid integrity check.

**See Also:** Constant Field Values

---

#### BAD_MIC

public static final int BAD_MIC

Token had invalid integrity check.

CONTEXT_EXPIRED

```java
public static final int CONTEXT_EXPIRED
```

Security context expired.

**See Also:** Constant Field Values

---

#### CONTEXT_EXPIRED

public static final int CONTEXT_EXPIRED

Security context expired.

CREDENTIALS_EXPIRED

```java
public static final int CREDENTIALS_EXPIRED
```

Expired credentials.

**See Also:** Constant Field Values

---

#### CREDENTIALS_EXPIRED

public static final int CREDENTIALS_EXPIRED

Expired credentials.

DEFECTIVE_CREDENTIAL

```java
public static final int DEFECTIVE_CREDENTIAL
```

Defective credentials.

**See Also:** Constant Field Values

---

#### DEFECTIVE_CREDENTIAL

public static final int DEFECTIVE_CREDENTIAL

Defective credentials.

DEFECTIVE_TOKEN

```java
public static final int DEFECTIVE_TOKEN
```

Defective token.

**See Also:** Constant Field Values

---

#### DEFECTIVE_TOKEN

public static final int DEFECTIVE_TOKEN

Defective token.

FAILURE

```java
public static final int FAILURE
```

General failure, unspecified at GSS-API level.

**See Also:** Constant Field Values

---

#### FAILURE

public static final int FAILURE

General failure, unspecified at GSS-API level.

NO_CONTEXT

```java
public static final int NO_CONTEXT
```

Invalid security context.

**See Also:** Constant Field Values

---

#### NO_CONTEXT

public static final int NO_CONTEXT

Invalid security context.

NO_CRED

```java
public static final int NO_CRED
```

Invalid credentials.

**See Also:** Constant Field Values

---

#### NO_CRED

public static final int NO_CRED

Invalid credentials.

BAD_QOP

```java
public static final int BAD_QOP
```

Unsupported QOP value.

**See Also:** Constant Field Values

---

#### BAD_QOP

public static final int BAD_QOP

Unsupported QOP value.

UNAUTHORIZED

```java
public static final int UNAUTHORIZED
```

Operation unauthorized.

**See Also:** Constant Field Values

---

#### UNAUTHORIZED

public static final int UNAUTHORIZED

Operation unauthorized.

UNAVAILABLE

```java
public static final int UNAVAILABLE
```

Operation unavailable.

**See Also:** Constant Field Values

---

#### UNAVAILABLE

public static final int UNAVAILABLE

Operation unavailable.

DUPLICATE_ELEMENT

```java
public static final int DUPLICATE_ELEMENT
```

Duplicate credential element requested.

**See Also:** Constant Field Values

---

#### DUPLICATE_ELEMENT

public static final int DUPLICATE_ELEMENT

Duplicate credential element requested.

NAME_NOT_MN

```java
public static final int NAME_NOT_MN
```

Name contains multi-mechanism elements.

**See Also:** Constant Field Values

---

#### NAME_NOT_MN

public static final int NAME_NOT_MN

Name contains multi-mechanism elements.

DUPLICATE_TOKEN

```java
public static final int DUPLICATE_TOKEN
```

The token was a duplicate of an earlier token.
This is a fatal error code that may occur during
context establishment. It is not used to indicate
supplementary status values. The MessageProp object is
used for that purpose.

**See Also:** Constant Field Values

---

#### DUPLICATE_TOKEN

public static final int DUPLICATE_TOKEN

The token was a duplicate of an earlier token.
This is a fatal error code that may occur during
context establishment. It is not used to indicate
supplementary status values. The MessageProp object is
used for that purpose.

OLD_TOKEN

```java
public static final int OLD_TOKEN
```

The token's validity period has expired. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

---

#### OLD_TOKEN

public static final int OLD_TOKEN

The token's validity period has expired. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

UNSEQ_TOKEN

```java
public static final int UNSEQ_TOKEN
```

A later token has already been processed. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

---

#### UNSEQ_TOKEN

public static final int UNSEQ_TOKEN

A later token has already been processed. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

GAP_TOKEN

```java
public static final int GAP_TOKEN
```

An expected per-message token was not received. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

**See Also:** Constant Field Values

---

#### GAP_TOKEN

public static final int GAP_TOKEN

An expected per-message token was not received. This is a
fatal error code that may occur during context establishment.
It is not used to indicate supplementary status values.
The MessageProp object is used for that purpose.

Constructor Detail

- GSSException

```java
public GSSException​(int majorCode)
```

Creates a GSSException object with a specified major code.

**Parameters:** majorCode

- the The GSS error code for the problem causing this
exception to be thrown.

- GSSException

```java
public GSSException​(int majorCode,
int minorCode,

String
minorString)
```

Creates a GSSException object with the specified major code, minor
code, and minor code textual explanation. This constructor is to be
used when the exception is originating from the underlying mechanism
level. It allows the setting of both the GSS code and the mechanism
code.

**Parameters:** majorCode

- the GSS error code for the problem causing this
exception to be thrown.
**Parameters:** minorCode

- the mechanism level error code for the problem
causing this exception to be thrown.
**Parameters:** minorString

- the textual explanation of the mechanism error
code.

---

#### Constructor Detail

GSSException

```java
public GSSException​(int majorCode)
```

Creates a GSSException object with a specified major code.

**Parameters:** majorCode

- the The GSS error code for the problem causing this
exception to be thrown.

---

#### GSSException

public GSSException​(int majorCode)

Creates a GSSException object with a specified major code.

GSSException

```java
public GSSException​(int majorCode,
int minorCode,

String
minorString)
```

Creates a GSSException object with the specified major code, minor
code, and minor code textual explanation. This constructor is to be
used when the exception is originating from the underlying mechanism
level. It allows the setting of both the GSS code and the mechanism
code.

**Parameters:** majorCode

- the GSS error code for the problem causing this
exception to be thrown.
**Parameters:** minorCode

- the mechanism level error code for the problem
causing this exception to be thrown.
**Parameters:** minorString

- the textual explanation of the mechanism error
code.

---

#### GSSException

public GSSException​(int majorCode,
int minorCode,

String

minorString)

Creates a GSSException object with the specified major code, minor
code, and minor code textual explanation. This constructor is to be
used when the exception is originating from the underlying mechanism
level. It allows the setting of both the GSS code and the mechanism
code.

Method Detail

- getMajor

```java
public int getMajor()
```

Returns the GSS-API level major error code for the problem causing
this exception to be thrown. Major error codes are
defined at the mechanism independent GSS-API level in this
class. Mechanism specific error codes that might provide more
information are set as the minor error code.

**Returns:** int the GSS-API level major error code causing this exception
**See Also:** getMajorString()

,

getMinor()

,

getMinorString()

- getMinor

```java
public int getMinor()
```

Returns the mechanism level error code for the problem causing this
exception to be thrown. The minor code is set by the underlying
mechanism.

**Returns:** int the mechanism error code; 0 indicates that it has not
been set.
**See Also:** getMinorString()

,

setMinor(int, java.lang.String)

- getMajorString

```java
public
String
getMajorString()
```

Returns a string explaining the GSS-API level major error code in
this exception.

**Returns:** String explanation string for the major error code
**See Also:** getMajor()

,

toString()

- getMinorString

```java
public
String
getMinorString()
```

Returns a string explaining the mechanism specific error code.
If the minor status code is 0, then no mechanism level error details
will be available.

**Returns:** String a textual explanation of mechanism error code
**See Also:** getMinor()

,

getMajorString()

,

toString()

- setMinor

```java
public void setMinor​(int minorCode,

String
message)
```

Used by the exception thrower to set the mechanism
level minor error code and its string explanation. This is used by
mechanism providers to indicate error details.

**Parameters:** minorCode

- the mechanism specific error code
**Parameters:** message

- textual explanation of the mechanism error code
**See Also:** getMinor()

- toString

```java
public
String
toString()
```

Returns a textual representation of both the major and the minor
status codes.

**Overrides:** toString

in class

Throwable
**Returns:** a String with the error descriptions

- getMessage

```java
public
String
getMessage()
```

Returns a textual representation of both the major and the minor
status codes.

**Overrides:** getMessage

in class

Throwable
**Returns:** a String with the error descriptions

---

#### Method Detail

getMajor

```java
public int getMajor()
```

Returns the GSS-API level major error code for the problem causing
this exception to be thrown. Major error codes are
defined at the mechanism independent GSS-API level in this
class. Mechanism specific error codes that might provide more
information are set as the minor error code.

**Returns:** int the GSS-API level major error code causing this exception
**See Also:** getMajorString()

,

getMinor()

,

getMinorString()

---

#### getMajor

public int getMajor()

Returns the GSS-API level major error code for the problem causing
this exception to be thrown. Major error codes are
defined at the mechanism independent GSS-API level in this
class. Mechanism specific error codes that might provide more
information are set as the minor error code.

getMinor

```java
public int getMinor()
```

Returns the mechanism level error code for the problem causing this
exception to be thrown. The minor code is set by the underlying
mechanism.

**Returns:** int the mechanism error code; 0 indicates that it has not
been set.
**See Also:** getMinorString()

,

setMinor(int, java.lang.String)

---

#### getMinor

public int getMinor()

Returns the mechanism level error code for the problem causing this
exception to be thrown. The minor code is set by the underlying
mechanism.

getMajorString

```java
public
String
getMajorString()
```

Returns a string explaining the GSS-API level major error code in
this exception.

**Returns:** String explanation string for the major error code
**See Also:** getMajor()

,

toString()

---

#### getMajorString

public

String

getMajorString()

Returns a string explaining the GSS-API level major error code in
this exception.

getMinorString

```java
public
String
getMinorString()
```

Returns a string explaining the mechanism specific error code.
If the minor status code is 0, then no mechanism level error details
will be available.

**Returns:** String a textual explanation of mechanism error code
**See Also:** getMinor()

,

getMajorString()

,

toString()

---

#### getMinorString

public

String

getMinorString()

Returns a string explaining the mechanism specific error code.
If the minor status code is 0, then no mechanism level error details
will be available.

setMinor

```java
public void setMinor​(int minorCode,

String
message)
```

Used by the exception thrower to set the mechanism
level minor error code and its string explanation. This is used by
mechanism providers to indicate error details.

**Parameters:** minorCode

- the mechanism specific error code
**Parameters:** message

- textual explanation of the mechanism error code
**See Also:** getMinor()

---

#### setMinor

public void setMinor​(int minorCode,

String

message)

Used by the exception thrower to set the mechanism
level minor error code and its string explanation. This is used by
mechanism providers to indicate error details.

toString

```java
public
String
toString()
```

Returns a textual representation of both the major and the minor
status codes.

**Overrides:** toString

in class

Throwable
**Returns:** a String with the error descriptions

---

#### toString

public

String

toString()

Returns a textual representation of both the major and the minor
status codes.

getMessage

```java
public
String
getMessage()
```

Returns a textual representation of both the major and the minor
status codes.

**Overrides:** getMessage

in class

Throwable
**Returns:** a String with the error descriptions

---

#### getMessage

public

String

getMessage()

Returns a textual representation of both the major and the minor
status codes.

---


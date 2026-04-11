# Class MessageProp

**Source:** `java.security.jgss\org\ietf\jgss\MessageProp.html`

### Class Description

```java
public class
MessageProp

extends
Object
```

This is a utility class used within the per-message GSSContext
methods to convey per-message properties.

When used with the GSSContext interface's wrap and getMIC methods, an
instance of this class is used to indicate the desired
Quality-of-Protection (QOP) and to request if confidentiality services
are to be applied to caller supplied data (wrap only). To request
default QOP, the value of 0 should be used for QOP.

When used with the unwrap and verifyMIC methods of the GSSContext
interface, an instance of this class will be used to indicate the
applied QOP and confidentiality services over the supplied message.
In the case of verifyMIC, the confidentiality state will always be

false

. Upon return from these methods, this object will also
contain any supplementary status values applicable to the processed
token. The supplementary status values can indicate old tokens, out
of sequence tokens, gap tokens or duplicate tokens.

**Since:** 1.4
**See Also:** GSSContext.wrap(byte[], int, int, org.ietf.jgss.MessageProp)

,

GSSContext.unwrap(byte[], int, int, org.ietf.jgss.MessageProp)

,

GSSContext.getMIC(byte[], int, int, org.ietf.jgss.MessageProp)

,

GSSContext.verifyMIC(byte[], int, int, byte[], int, int, org.ietf.jgss.MessageProp)

---

### Field Details

*No entries found.*

### Constructor Details

#### public MessageProp​(boolean privState)

Constructor which sets the desired privacy state. The QOP value used
is 0.

**Parameters:**
- privState

- the privacy (i.e. confidentiality) state

---

#### public MessageProp​(int qop,
boolean privState)

Constructor which sets the values for the qop and privacy state.

**Parameters:**
- qop

- the QOP value
- privState

- the privacy (i.e. confidentiality) state

---

### Method Details

#### public int getQOP()

Retrieves the QOP value.

**Returns:**
- an int representing the QOP value

**See Also:**
- setQOP(int)

---

#### public boolean getPrivacy()

Retrieves the privacy state.

**Returns:**
- true if the privacy (i.e., confidentiality) state is true,
false otherwise.

**See Also:**
- setPrivacy(boolean)

---

#### public void setQOP​(int qop)

Sets the QOP value.

**Parameters:**
- qop

- the int value to set the QOP to

**See Also:**
- getQOP()

---

#### public void setPrivacy​(boolean privState)

Sets the privacy state.

**Parameters:**
- privState

- true is the privacy (i.e., confidentiality) state
is true, false otherwise.

**See Also:**
- getPrivacy()

---

#### public boolean isDuplicateToken()

Tests if this is a duplicate of an earlier token.

**Returns:**
- true if this is a duplicate, false otherwise.

---

#### public boolean isOldToken()

Tests if this token's validity period has expired, i.e., the token
is too old to be checked for duplication.

**Returns:**
- true if the token's validity period has expired, false
otherwise.

---

#### public boolean isUnseqToken()

Tests if a later token had already been processed.

**Returns:**
- true if a later token had already been processed, false otherwise.

---

#### public boolean isGapToken()

Tests if an expected token was not received, i.e., one or more
predecessor tokens have not yet been successfully processed.

**Returns:**
- true if an expected per-message token was not received,
false otherwise.

---

#### public int getMinorStatus()

Retrieves the minor status code that the underlying mechanism might
have set for this per-message operation.

**Returns:**
- the int minor status

---

#### public
String
getMinorString()

Retrieves a string explaining the minor status code.

**Returns:**
- a String corresponding to the minor status
code.

null

will be returned when no minor status code
has been set.

---

#### public void setSupplementaryStates​(boolean duplicate,
boolean old,
boolean unseq,
boolean gap,
int minorStatus,

String
minorString)

This method sets the state for the supplementary information flags
and the minor status in MessageProp. It is not used by the
application but by the GSS implementation to return this information
to the caller of a per-message context method.

**Parameters:**
- duplicate

- true if the token was a duplicate of an earlier
token, false otherwise
- old

- true if the token's validity period has expired, false
otherwise
- unseq

- true if a later token has already been processed, false
otherwise
- gap

- true if one or more predecessor tokens have not yet been
successfully processed, false otherwise
- minorStatus

- the int minor status code for the per-message
operation
- minorString

- the textual representation of the minorStatus value

---

### Additional Sections

#### Class MessageProp

java.lang.Object

- org.ietf.jgss.MessageProp

org.ietf.jgss.MessageProp

```java
public class
MessageProp

extends
Object
```

This is a utility class used within the per-message GSSContext
methods to convey per-message properties.

When used with the GSSContext interface's wrap and getMIC methods, an
instance of this class is used to indicate the desired
Quality-of-Protection (QOP) and to request if confidentiality services
are to be applied to caller supplied data (wrap only). To request
default QOP, the value of 0 should be used for QOP.

When used with the unwrap and verifyMIC methods of the GSSContext
interface, an instance of this class will be used to indicate the
applied QOP and confidentiality services over the supplied message.
In the case of verifyMIC, the confidentiality state will always be

false

. Upon return from these methods, this object will also
contain any supplementary status values applicable to the processed
token. The supplementary status values can indicate old tokens, out
of sequence tokens, gap tokens or duplicate tokens.

**Since:** 1.4
**See Also:** GSSContext.wrap(byte[], int, int, org.ietf.jgss.MessageProp)

,

GSSContext.unwrap(byte[], int, int, org.ietf.jgss.MessageProp)

,

GSSContext.getMIC(byte[], int, int, org.ietf.jgss.MessageProp)

,

GSSContext.verifyMIC(byte[], int, int, byte[], int, int, org.ietf.jgss.MessageProp)

public class

MessageProp

extends

Object

This is a utility class used within the per-message GSSContext
methods to convey per-message properties.

When used with the GSSContext interface's wrap and getMIC methods, an
instance of this class is used to indicate the desired
Quality-of-Protection (QOP) and to request if confidentiality services
are to be applied to caller supplied data (wrap only). To request
default QOP, the value of 0 should be used for QOP.

When used with the unwrap and verifyMIC methods of the GSSContext
interface, an instance of this class will be used to indicate the
applied QOP and confidentiality services over the supplied message.
In the case of verifyMIC, the confidentiality state will always be

false

. Upon return from these methods, this object will also
contain any supplementary status values applicable to the processed
token. The supplementary status values can indicate old tokens, out
of sequence tokens, gap tokens or duplicate tokens.

When used with the GSSContext interface's wrap and getMIC methods, an
instance of this class is used to indicate the desired
Quality-of-Protection (QOP) and to request if confidentiality services
are to be applied to caller supplied data (wrap only). To request
default QOP, the value of 0 should be used for QOP.

When used with the unwrap and verifyMIC methods of the GSSContext
interface, an instance of this class will be used to indicate the
applied QOP and confidentiality services over the supplied message.
In the case of verifyMIC, the confidentiality state will always be

false

. Upon return from these methods, this object will also
contain any supplementary status values applicable to the processed
token. The supplementary status values can indicate old tokens, out
of sequence tokens, gap tokens or duplicate tokens.

When used with the unwrap and verifyMIC methods of the GSSContext
interface, an instance of this class will be used to indicate the
applied QOP and confidentiality services over the supplied message.
In the case of verifyMIC, the confidentiality state will always be

false

. Upon return from these methods, this object will also
contain any supplementary status values applicable to the processed
token. The supplementary status values can indicate old tokens, out
of sequence tokens, gap tokens or duplicate tokens.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MessageProp

​(boolean privState)

Constructor which sets the desired privacy state.

MessageProp

​(int qop,
boolean privState)

Constructor which sets the values for the qop and privacy state.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getMinorStatus

()

Retrieves the minor status code that the underlying mechanism might
have set for this per-message operation.

String

getMinorString

()

Retrieves a string explaining the minor status code.

boolean

getPrivacy

()

Retrieves the privacy state.

int

getQOP

()

Retrieves the QOP value.

boolean

isDuplicateToken

()

Tests if this is a duplicate of an earlier token.

boolean

isGapToken

()

Tests if an expected token was not received, i.e., one or more
predecessor tokens have not yet been successfully processed.

boolean

isOldToken

()

Tests if this token's validity period has expired, i.e., the token
is too old to be checked for duplication.

boolean

isUnseqToken

()

Tests if a later token had already been processed.

void

setPrivacy

​(boolean privState)

Sets the privacy state.

void

setQOP

​(int qop)

Sets the QOP value.

void

setSupplementaryStates

​(boolean duplicate,
boolean old,
boolean unseq,
boolean gap,
int minorStatus,

String

minorString)

This method sets the state for the supplementary information flags
and the minor status in MessageProp.

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

MessageProp

​(boolean privState)

Constructor which sets the desired privacy state.

MessageProp

​(int qop,
boolean privState)

Constructor which sets the values for the qop and privacy state.

---

#### Constructor Summary

Constructor which sets the desired privacy state.

Constructor which sets the values for the qop and privacy state.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getMinorStatus

()

Retrieves the minor status code that the underlying mechanism might
have set for this per-message operation.

String

getMinorString

()

Retrieves a string explaining the minor status code.

boolean

getPrivacy

()

Retrieves the privacy state.

int

getQOP

()

Retrieves the QOP value.

boolean

isDuplicateToken

()

Tests if this is a duplicate of an earlier token.

boolean

isGapToken

()

Tests if an expected token was not received, i.e., one or more
predecessor tokens have not yet been successfully processed.

boolean

isOldToken

()

Tests if this token's validity period has expired, i.e., the token
is too old to be checked for duplication.

boolean

isUnseqToken

()

Tests if a later token had already been processed.

void

setPrivacy

​(boolean privState)

Sets the privacy state.

void

setQOP

​(int qop)

Sets the QOP value.

void

setSupplementaryStates

​(boolean duplicate,
boolean old,
boolean unseq,
boolean gap,
int minorStatus,

String

minorString)

This method sets the state for the supplementary information flags
and the minor status in MessageProp.

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

Retrieves the minor status code that the underlying mechanism might
have set for this per-message operation.

Retrieves a string explaining the minor status code.

Retrieves the privacy state.

Retrieves the QOP value.

Tests if this is a duplicate of an earlier token.

Tests if an expected token was not received, i.e., one or more
predecessor tokens have not yet been successfully processed.

Tests if this token's validity period has expired, i.e., the token
is too old to be checked for duplication.

Tests if a later token had already been processed.

Sets the privacy state.

Sets the QOP value.

This method sets the state for the supplementary information flags
and the minor status in MessageProp.

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

- MessageProp

```java
public MessageProp​(boolean privState)
```

Constructor which sets the desired privacy state. The QOP value used
is 0.

**Parameters:** privState

- the privacy (i.e. confidentiality) state

- MessageProp

```java
public MessageProp​(int qop,
boolean privState)
```

Constructor which sets the values for the qop and privacy state.

**Parameters:** qop

- the QOP value
**Parameters:** privState

- the privacy (i.e. confidentiality) state

============ METHOD DETAIL ==========

- Method Detail

- getQOP

```java
public int getQOP()
```

Retrieves the QOP value.

**Returns:** an int representing the QOP value
**See Also:** setQOP(int)

- getPrivacy

```java
public boolean getPrivacy()
```

Retrieves the privacy state.

**Returns:** true if the privacy (i.e., confidentiality) state is true,
false otherwise.
**See Also:** setPrivacy(boolean)

- setQOP

```java
public void setQOP​(int qop)
```

Sets the QOP value.

**Parameters:** qop

- the int value to set the QOP to
**See Also:** getQOP()

- setPrivacy

```java
public void setPrivacy​(boolean privState)
```

Sets the privacy state.

**Parameters:** privState

- true is the privacy (i.e., confidentiality) state
is true, false otherwise.
**See Also:** getPrivacy()

- isDuplicateToken

```java
public boolean isDuplicateToken()
```

Tests if this is a duplicate of an earlier token.

**Returns:** true if this is a duplicate, false otherwise.

- isOldToken

```java
public boolean isOldToken()
```

Tests if this token's validity period has expired, i.e., the token
is too old to be checked for duplication.

**Returns:** true if the token's validity period has expired, false
otherwise.

- isUnseqToken

```java
public boolean isUnseqToken()
```

Tests if a later token had already been processed.

**Returns:** true if a later token had already been processed, false otherwise.

- isGapToken

```java
public boolean isGapToken()
```

Tests if an expected token was not received, i.e., one or more
predecessor tokens have not yet been successfully processed.

**Returns:** true if an expected per-message token was not received,
false otherwise.

- getMinorStatus

```java
public int getMinorStatus()
```

Retrieves the minor status code that the underlying mechanism might
have set for this per-message operation.

**Returns:** the int minor status

- getMinorString

```java
public
String
getMinorString()
```

Retrieves a string explaining the minor status code.

**Returns:** a String corresponding to the minor status
code.

null

will be returned when no minor status code
has been set.

- setSupplementaryStates

```java
public void setSupplementaryStates​(boolean duplicate,
boolean old,
boolean unseq,
boolean gap,
int minorStatus,

String
minorString)
```

This method sets the state for the supplementary information flags
and the minor status in MessageProp. It is not used by the
application but by the GSS implementation to return this information
to the caller of a per-message context method.

**Parameters:** duplicate

- true if the token was a duplicate of an earlier
token, false otherwise
**Parameters:** old

- true if the token's validity period has expired, false
otherwise
**Parameters:** unseq

- true if a later token has already been processed, false
otherwise
**Parameters:** gap

- true if one or more predecessor tokens have not yet been
successfully processed, false otherwise
**Parameters:** minorStatus

- the int minor status code for the per-message
operation
**Parameters:** minorString

- the textual representation of the minorStatus value

Constructor Detail

- MessageProp

```java
public MessageProp​(boolean privState)
```

Constructor which sets the desired privacy state. The QOP value used
is 0.

**Parameters:** privState

- the privacy (i.e. confidentiality) state

- MessageProp

```java
public MessageProp​(int qop,
boolean privState)
```

Constructor which sets the values for the qop and privacy state.

**Parameters:** qop

- the QOP value
**Parameters:** privState

- the privacy (i.e. confidentiality) state

---

#### Constructor Detail

MessageProp

```java
public MessageProp​(boolean privState)
```

Constructor which sets the desired privacy state. The QOP value used
is 0.

**Parameters:** privState

- the privacy (i.e. confidentiality) state

---

#### MessageProp

public MessageProp​(boolean privState)

Constructor which sets the desired privacy state. The QOP value used
is 0.

MessageProp

```java
public MessageProp​(int qop,
boolean privState)
```

Constructor which sets the values for the qop and privacy state.

**Parameters:** qop

- the QOP value
**Parameters:** privState

- the privacy (i.e. confidentiality) state

---

#### MessageProp

public MessageProp​(int qop,
boolean privState)

Constructor which sets the values for the qop and privacy state.

Method Detail

- getQOP

```java
public int getQOP()
```

Retrieves the QOP value.

**Returns:** an int representing the QOP value
**See Also:** setQOP(int)

- getPrivacy

```java
public boolean getPrivacy()
```

Retrieves the privacy state.

**Returns:** true if the privacy (i.e., confidentiality) state is true,
false otherwise.
**See Also:** setPrivacy(boolean)

- setQOP

```java
public void setQOP​(int qop)
```

Sets the QOP value.

**Parameters:** qop

- the int value to set the QOP to
**See Also:** getQOP()

- setPrivacy

```java
public void setPrivacy​(boolean privState)
```

Sets the privacy state.

**Parameters:** privState

- true is the privacy (i.e., confidentiality) state
is true, false otherwise.
**See Also:** getPrivacy()

- isDuplicateToken

```java
public boolean isDuplicateToken()
```

Tests if this is a duplicate of an earlier token.

**Returns:** true if this is a duplicate, false otherwise.

- isOldToken

```java
public boolean isOldToken()
```

Tests if this token's validity period has expired, i.e., the token
is too old to be checked for duplication.

**Returns:** true if the token's validity period has expired, false
otherwise.

- isUnseqToken

```java
public boolean isUnseqToken()
```

Tests if a later token had already been processed.

**Returns:** true if a later token had already been processed, false otherwise.

- isGapToken

```java
public boolean isGapToken()
```

Tests if an expected token was not received, i.e., one or more
predecessor tokens have not yet been successfully processed.

**Returns:** true if an expected per-message token was not received,
false otherwise.

- getMinorStatus

```java
public int getMinorStatus()
```

Retrieves the minor status code that the underlying mechanism might
have set for this per-message operation.

**Returns:** the int minor status

- getMinorString

```java
public
String
getMinorString()
```

Retrieves a string explaining the minor status code.

**Returns:** a String corresponding to the minor status
code.

null

will be returned when no minor status code
has been set.

- setSupplementaryStates

```java
public void setSupplementaryStates​(boolean duplicate,
boolean old,
boolean unseq,
boolean gap,
int minorStatus,

String
minorString)
```

This method sets the state for the supplementary information flags
and the minor status in MessageProp. It is not used by the
application but by the GSS implementation to return this information
to the caller of a per-message context method.

**Parameters:** duplicate

- true if the token was a duplicate of an earlier
token, false otherwise
**Parameters:** old

- true if the token's validity period has expired, false
otherwise
**Parameters:** unseq

- true if a later token has already been processed, false
otherwise
**Parameters:** gap

- true if one or more predecessor tokens have not yet been
successfully processed, false otherwise
**Parameters:** minorStatus

- the int minor status code for the per-message
operation
**Parameters:** minorString

- the textual representation of the minorStatus value

---

#### Method Detail

getQOP

```java
public int getQOP()
```

Retrieves the QOP value.

**Returns:** an int representing the QOP value
**See Also:** setQOP(int)

---

#### getQOP

public int getQOP()

Retrieves the QOP value.

getPrivacy

```java
public boolean getPrivacy()
```

Retrieves the privacy state.

**Returns:** true if the privacy (i.e., confidentiality) state is true,
false otherwise.
**See Also:** setPrivacy(boolean)

---

#### getPrivacy

public boolean getPrivacy()

Retrieves the privacy state.

setQOP

```java
public void setQOP​(int qop)
```

Sets the QOP value.

**Parameters:** qop

- the int value to set the QOP to
**See Also:** getQOP()

---

#### setQOP

public void setQOP​(int qop)

Sets the QOP value.

setPrivacy

```java
public void setPrivacy​(boolean privState)
```

Sets the privacy state.

**Parameters:** privState

- true is the privacy (i.e., confidentiality) state
is true, false otherwise.
**See Also:** getPrivacy()

---

#### setPrivacy

public void setPrivacy​(boolean privState)

Sets the privacy state.

isDuplicateToken

```java
public boolean isDuplicateToken()
```

Tests if this is a duplicate of an earlier token.

**Returns:** true if this is a duplicate, false otherwise.

---

#### isDuplicateToken

public boolean isDuplicateToken()

Tests if this is a duplicate of an earlier token.

isOldToken

```java
public boolean isOldToken()
```

Tests if this token's validity period has expired, i.e., the token
is too old to be checked for duplication.

**Returns:** true if the token's validity period has expired, false
otherwise.

---

#### isOldToken

public boolean isOldToken()

Tests if this token's validity period has expired, i.e., the token
is too old to be checked for duplication.

isUnseqToken

```java
public boolean isUnseqToken()
```

Tests if a later token had already been processed.

**Returns:** true if a later token had already been processed, false otherwise.

---

#### isUnseqToken

public boolean isUnseqToken()

Tests if a later token had already been processed.

isGapToken

```java
public boolean isGapToken()
```

Tests if an expected token was not received, i.e., one or more
predecessor tokens have not yet been successfully processed.

**Returns:** true if an expected per-message token was not received,
false otherwise.

---

#### isGapToken

public boolean isGapToken()

Tests if an expected token was not received, i.e., one or more
predecessor tokens have not yet been successfully processed.

getMinorStatus

```java
public int getMinorStatus()
```

Retrieves the minor status code that the underlying mechanism might
have set for this per-message operation.

**Returns:** the int minor status

---

#### getMinorStatus

public int getMinorStatus()

Retrieves the minor status code that the underlying mechanism might
have set for this per-message operation.

getMinorString

```java
public
String
getMinorString()
```

Retrieves a string explaining the minor status code.

**Returns:** a String corresponding to the minor status
code.

null

will be returned when no minor status code
has been set.

---

#### getMinorString

public

String

getMinorString()

Retrieves a string explaining the minor status code.

setSupplementaryStates

```java
public void setSupplementaryStates​(boolean duplicate,
boolean old,
boolean unseq,
boolean gap,
int minorStatus,

String
minorString)
```

This method sets the state for the supplementary information flags
and the minor status in MessageProp. It is not used by the
application but by the GSS implementation to return this information
to the caller of a per-message context method.

**Parameters:** duplicate

- true if the token was a duplicate of an earlier
token, false otherwise
**Parameters:** old

- true if the token's validity period has expired, false
otherwise
**Parameters:** unseq

- true if a later token has already been processed, false
otherwise
**Parameters:** gap

- true if one or more predecessor tokens have not yet been
successfully processed, false otherwise
**Parameters:** minorStatus

- the int minor status code for the per-message
operation
**Parameters:** minorString

- the textual representation of the minorStatus value

---

#### setSupplementaryStates

public void setSupplementaryStates​(boolean duplicate,
boolean old,
boolean unseq,
boolean gap,
int minorStatus,

String

minorString)

This method sets the state for the supplementary information flags
and the minor status in MessageProp. It is not used by the
application but by the GSS implementation to return this information
to the caller of a per-message context method.

---


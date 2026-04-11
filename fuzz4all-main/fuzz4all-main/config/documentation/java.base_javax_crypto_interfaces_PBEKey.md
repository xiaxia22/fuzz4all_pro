# Interface PBEKey

**Source:** `java.base\javax\crypto\interfaces\PBEKey.html`

### Class Description

```java
public interface
PBEKey

extends
SecretKey
```

The interface to a PBE key.

**All Superinterfaces:** Destroyable

,

Key

,

SecretKey

,

Serializable

---

### Field Details

#### static final long serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### char[] getPassword()

Returns the password.

Note: this method should return a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:**
- the password.

---

#### byte[] getSalt()

Returns the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

**Returns:**
- the salt.

---

#### int getIterationCount()

Returns the iteration count or 0 if not specified.

**Returns:**
- the iteration count.

---

### Additional Sections

#### Interface PBEKey

**All Superinterfaces:** Destroyable

,

Key

,

SecretKey

,

Serializable

```java
public interface
PBEKey

extends
SecretKey
```

The interface to a PBE key.

**Since:** 1.4
**See Also:** PBEKeySpec

,

SecretKey

public interface

PBEKey

extends

SecretKey

The interface to a PBE key.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getIterationCount

()

Returns the iteration count or 0 if not specified.

char[]

getPassword

()

Returns the password.

byte[]

getSalt

()

Returns the salt or null if not specified.

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

---

#### Field Summary

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getIterationCount

()

Returns the iteration count or 0 if not specified.

char[]

getPassword

()

Returns the password.

byte[]

getSalt

()

Returns the salt or null if not specified.

- Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

---

#### Method Summary

Returns the iteration count or 0 if not specified.

Returns the password.

Returns the salt or null if not specified.

Methods declared in interface javax.security.auth.

Destroyable

destroy

,

isDestroyed

---

#### Methods declared in interface javax.security.auth. Destroyable

Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

---

#### Methods declared in interface java.security. Key

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getPassword

```java
char[] getPassword()
```

Returns the password.

Note: this method should return a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password.

- getSalt

```java
byte[] getSalt()
```

Returns the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

**Returns:** the salt.

- getIterationCount

```java
int getIterationCount()
```

Returns the iteration count or 0 if not specified.

**Returns:** the iteration count.

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

The class fingerprint that is set to indicate serialization
compatibility since J2SE 1.4.

Method Detail

- getPassword

```java
char[] getPassword()
```

Returns the password.

Note: this method should return a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password.

- getSalt

```java
byte[] getSalt()
```

Returns the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

**Returns:** the salt.

- getIterationCount

```java
int getIterationCount()
```

Returns the iteration count or 0 if not specified.

**Returns:** the iteration count.

---

#### Method Detail

getPassword

```java
char[] getPassword()
```

Returns the password.

Note: this method should return a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

**Returns:** the password.

---

#### getPassword

char[] getPassword()

Returns the password.

Note: this method should return a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

Note: this method should return a copy of the password. It is
the caller's responsibility to zero out the password information after
it is no longer needed.

getSalt

```java
byte[] getSalt()
```

Returns the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

**Returns:** the salt.

---

#### getSalt

byte[] getSalt()

Returns the salt or null if not specified.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

Note: this method should return a copy of the salt. It is
the caller's responsibility to zero out the salt information after
it is no longer needed.

getIterationCount

```java
int getIterationCount()
```

Returns the iteration count or 0 if not specified.

**Returns:** the iteration count.

---

#### getIterationCount

int getIterationCount()

Returns the iteration count or 0 if not specified.

---


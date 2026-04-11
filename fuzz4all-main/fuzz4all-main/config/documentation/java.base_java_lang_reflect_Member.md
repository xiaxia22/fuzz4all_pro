# Interface Member

**Source:** `java.base\java\lang\reflect\Member.html`

### Class Description

```java
public interface
Member
```

Member is an interface that reflects identifying information about
a single member (a field or a method) or a constructor.

**All Known Implementing Classes:** Constructor

,

Executable

,

Field

,

Method

---

### Field Details

#### static final int PUBLIC

Identifies the set of all public members of a class or interface,
including inherited members.

**See Also:**
- Constant Field Values

---

#### static final int DECLARED

Identifies the set of declared members of a class or interface.
Inherited members are not included.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Class
<?> getDeclaringClass()

Returns the Class object representing the class or interface
that declares the member or constructor represented by this Member.

**Returns:**
- an object representing the declaring class of the
underlying member

---

#### String
getName()

Returns the simple name of the underlying member or constructor
represented by this Member.

**Returns:**
- the simple name of the underlying member

---

#### int getModifiers()

Returns the Java language modifiers for the member or
constructor represented by this Member, as an integer. The
Modifier class should be used to decode the modifiers in
the integer.

**Returns:**
- the Java language modifiers for the underlying member

**See Also:**
- Modifier

---

#### boolean isSynthetic()

Returns

true

if this member was introduced by
the compiler; returns

false

otherwise.

**Returns:**
- true if and only if this member was introduced by
the compiler.

**Since:**
- 1.5

**See The Java™ Language Specification :**
- 13.1 The Form of a Binary

---

### Additional Sections

#### Interface Member

**All Known Implementing Classes:** Constructor

,

Executable

,

Field

,

Method

```java
public interface
Member
```

Member is an interface that reflects identifying information about
a single member (a field or a method) or a constructor.

**Since:** 1.1
**See Also:** Class

,

Field

,

Method

,

Constructor

public interface

Member

Member is an interface that reflects identifying information about
a single member (a field or a method) or a constructor.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DECLARED

Identifies the set of declared members of a class or interface.

static int

PUBLIC

Identifies the set of all public members of a class or interface,
including inherited members.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<?>

getDeclaringClass

()

Returns the Class object representing the class or interface
that declares the member or constructor represented by this Member.

int

getModifiers

()

Returns the Java language modifiers for the member or
constructor represented by this Member, as an integer.

String

getName

()

Returns the simple name of the underlying member or constructor
represented by this Member.

boolean

isSynthetic

()

Returns

true

if this member was introduced by
the compiler; returns

false

otherwise.

Field Summary

Fields

Modifier and Type

Field

Description

static int

DECLARED

Identifies the set of declared members of a class or interface.

static int

PUBLIC

Identifies the set of all public members of a class or interface,
including inherited members.

---

#### Field Summary

Identifies the set of declared members of a class or interface.

Identifies the set of all public members of a class or interface,
including inherited members.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<?>

getDeclaringClass

()

Returns the Class object representing the class or interface
that declares the member or constructor represented by this Member.

int

getModifiers

()

Returns the Java language modifiers for the member or
constructor represented by this Member, as an integer.

String

getName

()

Returns the simple name of the underlying member or constructor
represented by this Member.

boolean

isSynthetic

()

Returns

true

if this member was introduced by
the compiler; returns

false

otherwise.

---

#### Method Summary

Returns the Class object representing the class or interface
that declares the member or constructor represented by this Member.

Returns the Java language modifiers for the member or
constructor represented by this Member, as an integer.

Returns the simple name of the underlying member or constructor
represented by this Member.

Returns

true

if this member was introduced by
the compiler; returns

false

otherwise.

============ FIELD DETAIL ===========

- Field Detail

- PUBLIC

```java
static final int PUBLIC
```

Identifies the set of all public members of a class or interface,
including inherited members.

**See Also:** Constant Field Values

- DECLARED

```java
static final int DECLARED
```

Identifies the set of declared members of a class or interface.
Inherited members are not included.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getDeclaringClass

```java
Class
<?> getDeclaringClass()
```

Returns the Class object representing the class or interface
that declares the member or constructor represented by this Member.

**Returns:** an object representing the declaring class of the
underlying member

- getName

```java
String
getName()
```

Returns the simple name of the underlying member or constructor
represented by this Member.

**Returns:** the simple name of the underlying member

- getModifiers

```java
int getModifiers()
```

Returns the Java language modifiers for the member or
constructor represented by this Member, as an integer. The
Modifier class should be used to decode the modifiers in
the integer.

**Returns:** the Java language modifiers for the underlying member
**See Also:** Modifier

- isSynthetic

```java
boolean isSynthetic()
```

Returns

true

if this member was introduced by
the compiler; returns

false

otherwise.

**Returns:** true if and only if this member was introduced by
the compiler.
**Since:** 1.5
**See The Java™ Language Specification :** 13.1 The Form of a Binary

Field Detail

- PUBLIC

```java
static final int PUBLIC
```

Identifies the set of all public members of a class or interface,
including inherited members.

**See Also:** Constant Field Values

- DECLARED

```java
static final int DECLARED
```

Identifies the set of declared members of a class or interface.
Inherited members are not included.

**See Also:** Constant Field Values

---

#### Field Detail

PUBLIC

```java
static final int PUBLIC
```

Identifies the set of all public members of a class or interface,
including inherited members.

**See Also:** Constant Field Values

---

#### PUBLIC

static final int PUBLIC

Identifies the set of all public members of a class or interface,
including inherited members.

DECLARED

```java
static final int DECLARED
```

Identifies the set of declared members of a class or interface.
Inherited members are not included.

**See Also:** Constant Field Values

---

#### DECLARED

static final int DECLARED

Identifies the set of declared members of a class or interface.
Inherited members are not included.

Method Detail

- getDeclaringClass

```java
Class
<?> getDeclaringClass()
```

Returns the Class object representing the class or interface
that declares the member or constructor represented by this Member.

**Returns:** an object representing the declaring class of the
underlying member

- getName

```java
String
getName()
```

Returns the simple name of the underlying member or constructor
represented by this Member.

**Returns:** the simple name of the underlying member

- getModifiers

```java
int getModifiers()
```

Returns the Java language modifiers for the member or
constructor represented by this Member, as an integer. The
Modifier class should be used to decode the modifiers in
the integer.

**Returns:** the Java language modifiers for the underlying member
**See Also:** Modifier

- isSynthetic

```java
boolean isSynthetic()
```

Returns

true

if this member was introduced by
the compiler; returns

false

otherwise.

**Returns:** true if and only if this member was introduced by
the compiler.
**Since:** 1.5
**See The Java™ Language Specification :** 13.1 The Form of a Binary

---

#### Method Detail

getDeclaringClass

```java
Class
<?> getDeclaringClass()
```

Returns the Class object representing the class or interface
that declares the member or constructor represented by this Member.

**Returns:** an object representing the declaring class of the
underlying member

---

#### getDeclaringClass

Class

<?> getDeclaringClass()

Returns the Class object representing the class or interface
that declares the member or constructor represented by this Member.

getName

```java
String
getName()
```

Returns the simple name of the underlying member or constructor
represented by this Member.

**Returns:** the simple name of the underlying member

---

#### getName

String

getName()

Returns the simple name of the underlying member or constructor
represented by this Member.

getModifiers

```java
int getModifiers()
```

Returns the Java language modifiers for the member or
constructor represented by this Member, as an integer. The
Modifier class should be used to decode the modifiers in
the integer.

**Returns:** the Java language modifiers for the underlying member
**See Also:** Modifier

---

#### getModifiers

int getModifiers()

Returns the Java language modifiers for the member or
constructor represented by this Member, as an integer. The
Modifier class should be used to decode the modifiers in
the integer.

isSynthetic

```java
boolean isSynthetic()
```

Returns

true

if this member was introduced by
the compiler; returns

false

otherwise.

**Returns:** true if and only if this member was introduced by
the compiler.
**Since:** 1.5
**See The Java™ Language Specification :** 13.1 The Form of a Binary

---

#### isSynthetic

boolean isSynthetic()

Returns

true

if this member was introduced by
the compiler; returns

false

otherwise.

---


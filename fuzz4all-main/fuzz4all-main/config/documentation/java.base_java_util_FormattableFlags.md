# Class FormattableFlags

**Source:** `java.base\java\util\FormattableFlags.html`

### Class Description

```java
public class
FormattableFlags

extends
Object
```

FormattableFlags are passed to the

Formattable.formatTo()

method and modify the output format for

Formattables

. Implementations of

Formattable

are
responsible for interpreting and validating any flags.

**Since:** 1.5

---

### Field Details

#### public static final int LEFT_JUSTIFY

Left-justifies the output. Spaces (

'\u0020'

) will be added
at the end of the converted value as required to fill the minimum width
of the field. If this flag is not set then the output will be
right-justified.

This flag corresponds to

'-'

(

'\u002d'

) in
the format specifier.

**See Also:**
- Constant Field Values

---

#### public static final int UPPERCASE

Converts the output to upper case according to the rules of the

locale

given during creation of the

formatter

argument of the

formatTo()

method. The output should be equivalent the following
invocation of

String.toUpperCase(java.util.Locale)

```java
out.toUpperCase()
```

This flag corresponds to

'S'

(

'\u0053'

) in
the format specifier.

**See Also:**
- Constant Field Values

---

#### public static final int ALTERNATE

Requires the output to use an alternate form. The definition of the
form is specified by the

Formattable

.

This flag corresponds to

'#'

(

'\u0023'

) in
the format specifier.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class FormattableFlags

java.lang.Object

- java.util.FormattableFlags

java.util.FormattableFlags

```java
public class
FormattableFlags

extends
Object
```

FormattableFlags are passed to the

Formattable.formatTo()

method and modify the output format for

Formattables

. Implementations of

Formattable

are
responsible for interpreting and validating any flags.

**Since:** 1.5

public class

FormattableFlags

extends

Object

FormattableFlags are passed to the

Formattable.formatTo()

method and modify the output format for

Formattables

. Implementations of

Formattable

are
responsible for interpreting and validating any flags.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALTERNATE

Requires the output to use an alternate form.

static int

LEFT_JUSTIFY

Left-justifies the output.

static int

UPPERCASE

Converts the output to upper case according to the rules of the

locale

given during creation of the

formatter

argument of the

formatTo()

method.

========== METHOD SUMMARY ===========

- Method Summary

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ALTERNATE

Requires the output to use an alternate form.

static int

LEFT_JUSTIFY

Left-justifies the output.

static int

UPPERCASE

Converts the output to upper case according to the rules of the

locale

given during creation of the

formatter

argument of the

formatTo()

method.

---

#### Field Summary

Requires the output to use an alternate form.

Left-justifies the output.

Converts the output to upper case according to the rules of the

locale

given during creation of the

formatter

argument of the

formatTo()

method.

Method Summary

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

============ FIELD DETAIL ===========

- Field Detail

- LEFT_JUSTIFY

```java
public static final int LEFT_JUSTIFY
```

Left-justifies the output. Spaces (

'\u0020'

) will be added
at the end of the converted value as required to fill the minimum width
of the field. If this flag is not set then the output will be
right-justified.

This flag corresponds to

'-'

(

'\u002d'

) in
the format specifier.

**See Also:** Constant Field Values

- UPPERCASE

```java
public static final int UPPERCASE
```

Converts the output to upper case according to the rules of the

locale

given during creation of the

formatter

argument of the

formatTo()

method. The output should be equivalent the following
invocation of

String.toUpperCase(java.util.Locale)

```java
out.toUpperCase()
```

This flag corresponds to

'S'

(

'\u0053'

) in
the format specifier.

**See Also:** Constant Field Values

- ALTERNATE

```java
public static final int ALTERNATE
```

Requires the output to use an alternate form. The definition of the
form is specified by the

Formattable

.

This flag corresponds to

'#'

(

'\u0023'

) in
the format specifier.

**See Also:** Constant Field Values

Field Detail

- LEFT_JUSTIFY

```java
public static final int LEFT_JUSTIFY
```

Left-justifies the output. Spaces (

'\u0020'

) will be added
at the end of the converted value as required to fill the minimum width
of the field. If this flag is not set then the output will be
right-justified.

This flag corresponds to

'-'

(

'\u002d'

) in
the format specifier.

**See Also:** Constant Field Values

- UPPERCASE

```java
public static final int UPPERCASE
```

Converts the output to upper case according to the rules of the

locale

given during creation of the

formatter

argument of the

formatTo()

method. The output should be equivalent the following
invocation of

String.toUpperCase(java.util.Locale)

```java
out.toUpperCase()
```

This flag corresponds to

'S'

(

'\u0053'

) in
the format specifier.

**See Also:** Constant Field Values

- ALTERNATE

```java
public static final int ALTERNATE
```

Requires the output to use an alternate form. The definition of the
form is specified by the

Formattable

.

This flag corresponds to

'#'

(

'\u0023'

) in
the format specifier.

**See Also:** Constant Field Values

---

#### Field Detail

LEFT_JUSTIFY

```java
public static final int LEFT_JUSTIFY
```

Left-justifies the output. Spaces (

'\u0020'

) will be added
at the end of the converted value as required to fill the minimum width
of the field. If this flag is not set then the output will be
right-justified.

This flag corresponds to

'-'

(

'\u002d'

) in
the format specifier.

**See Also:** Constant Field Values

---

#### LEFT_JUSTIFY

public static final int LEFT_JUSTIFY

Left-justifies the output. Spaces (

'\u0020'

) will be added
at the end of the converted value as required to fill the minimum width
of the field. If this flag is not set then the output will be
right-justified.

This flag corresponds to

'-'

(

'\u002d'

) in
the format specifier.

This flag corresponds to

'-'

(

'\u002d'

) in
the format specifier.

UPPERCASE

```java
public static final int UPPERCASE
```

Converts the output to upper case according to the rules of the

locale

given during creation of the

formatter

argument of the

formatTo()

method. The output should be equivalent the following
invocation of

String.toUpperCase(java.util.Locale)

```java
out.toUpperCase()
```

This flag corresponds to

'S'

(

'\u0053'

) in
the format specifier.

**See Also:** Constant Field Values

---

#### UPPERCASE

public static final int UPPERCASE

Converts the output to upper case according to the rules of the

locale

given during creation of the

formatter

argument of the

formatTo()

method. The output should be equivalent the following
invocation of

String.toUpperCase(java.util.Locale)

```java
out.toUpperCase()
```

This flag corresponds to

'S'

(

'\u0053'

) in
the format specifier.

out.toUpperCase()

This flag corresponds to

'S'

(

'\u0053'

) in
the format specifier.

ALTERNATE

```java
public static final int ALTERNATE
```

Requires the output to use an alternate form. The definition of the
form is specified by the

Formattable

.

This flag corresponds to

'#'

(

'\u0023'

) in
the format specifier.

**See Also:** Constant Field Values

---

#### ALTERNATE

public static final int ALTERNATE

Requires the output to use an alternate form. The definition of the
form is specified by the

Formattable

.

This flag corresponds to

'#'

(

'\u0023'

) in
the format specifier.

This flag corresponds to

'#'

(

'\u0023'

) in
the format specifier.

---


# Class Doclet

**Source:** `jdk.javadoc\com\sun\javadoc\Doclet.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public abstract class
Doclet

extends
Object
```

This is an example of a starting class for a doclet,
showing the entry-point methods. A starting class must
import com.sun.javadoc.* and implement the

start(RootDoc)

method, as described in the

package
description

. If the doclet takes command line options,
it must also implement

optionLength

and

validOptions

.

A doclet supporting the language features added since 1.1
(such as generics and annotations) should indicate this
by implementing

languageVersion

. In the absence of
this the doclet should not invoke any of the Doclet API methods
added since 1.5, and
the results of several other methods are modified so as
to conceal the new constructs (such as type parameters) from
the doclet.

To start the doclet, pass

-doclet

followed by the fully-qualified
name of the starting class on the javadoc tool command line.

---

### Field Details

*No entries found.*

### Constructor Details

#### public Doclet()

*No description found.*

---

### Method Details

#### public static boolean start​(
RootDoc
root)

Generate documentation here.
This method is required for all doclets.

**Parameters:**
- root

- Supply the RootDoc to the method.

**Returns:**
- true on success.

---

#### public static int optionLength​(
String
option)

Check for doclet-added options. Returns the number of
arguments you must specify on the command line for the
given option. For example, "-d docs" would return 2.

This method is required if the doclet contains any options.
If this method is missing, Javadoc will print an invalid flag
error for every option.

**Parameters:**
- option

- the option for which the number of arguements is returned.

**Returns:**
- number of arguments on the command line for an option
including the option name itself. Zero return means
option not known. Negative value means error occurred.

---

#### public static boolean validOptions​(
String
[][] options,

DocErrorReporter
reporter)

Check that options have the correct arguments.

This method is not required, but is recommended,
as every option will be considered valid if this method
is not present. It will default gracefully (to true)
if absent.

Printing option related error messages (using the provided
DocErrorReporter) is the responsibility of this method.

**Parameters:**
- options

- Supply valid options as an array of Strings.
- reporter

- The DocErrorReporter responsible for these options.

**Returns:**
- true if the options are valid.

---

#### public static
LanguageVersion
languageVersion()

Return the version of the Java Programming Language supported
by this doclet.

This method is required by any doclet supporting a language version
newer than 1.1.

**Returns:**
- the language version supported by this doclet.

**Since:**
- 1.5

---

### Additional Sections

#### Class Doclet

java.lang.Object

- com.sun.javadoc.Doclet

com.sun.javadoc.Doclet

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public abstract class
Doclet

extends
Object
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

This is an example of a starting class for a doclet,
showing the entry-point methods. A starting class must
import com.sun.javadoc.* and implement the

start(RootDoc)

method, as described in the

package
description

. If the doclet takes command line options,
it must also implement

optionLength

and

validOptions

.

A doclet supporting the language features added since 1.1
(such as generics and annotations) should indicate this
by implementing

languageVersion

. In the absence of
this the doclet should not invoke any of the Doclet API methods
added since 1.5, and
the results of several other methods are modified so as
to conceal the new constructs (such as type parameters) from
the doclet.

To start the doclet, pass

-doclet

followed by the fully-qualified
name of the starting class on the javadoc tool command line.

@Deprecated

(

since

="9",

forRemoval

=true)
public abstract class

Doclet

extends

Object

This is an example of a starting class for a doclet,
showing the entry-point methods. A starting class must
import com.sun.javadoc.* and implement the

start(RootDoc)

method, as described in the

package
description

. If the doclet takes command line options,
it must also implement

optionLength

and

validOptions

.

A doclet supporting the language features added since 1.1
(such as generics and annotations) should indicate this
by implementing

languageVersion

. In the absence of
this the doclet should not invoke any of the Doclet API methods
added since 1.5, and
the results of several other methods are modified so as
to conceal the new constructs (such as type parameters) from
the doclet.

To start the doclet, pass

-doclet

followed by the fully-qualified
name of the starting class on the javadoc tool command line.

A doclet supporting the language features added since 1.1
(such as generics and annotations) should indicate this
by implementing

languageVersion

. In the absence of
this the doclet should not invoke any of the Doclet API methods
added since 1.5, and
the results of several other methods are modified so as
to conceal the new constructs (such as type parameters) from
the doclet.

To start the doclet, pass

-doclet

followed by the fully-qualified
name of the starting class on the javadoc tool command line.

To start the doclet, pass

-doclet

followed by the fully-qualified
name of the starting class on the javadoc tool command line.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Doclet

()

Deprecated, for removal: This API element is subject to removal in a future version.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

LanguageVersion

languageVersion

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the version of the Java Programming Language supported
by this doclet.

static int

optionLength

​(

String

option)

Deprecated, for removal: This API element is subject to removal in a future version.

Check for doclet-added options.

static boolean

start

​(

RootDoc

root)

Deprecated, for removal: This API element is subject to removal in a future version.

Generate documentation here.

static boolean

validOptions

​(

String

[][] options,

DocErrorReporter

reporter)

Deprecated, for removal: This API element is subject to removal in a future version.

Check that options have the correct arguments.

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

Doclet

()

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

LanguageVersion

languageVersion

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the version of the Java Programming Language supported
by this doclet.

static int

optionLength

​(

String

option)

Deprecated, for removal: This API element is subject to removal in a future version.

Check for doclet-added options.

static boolean

start

​(

RootDoc

root)

Deprecated, for removal: This API element is subject to removal in a future version.

Generate documentation here.

static boolean

validOptions

​(

String

[][] options,

DocErrorReporter

reporter)

Deprecated, for removal: This API element is subject to removal in a future version.

Check that options have the correct arguments.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Return the version of the Java Programming Language supported
by this doclet.

Check for doclet-added options.

Generate documentation here.

Check that options have the correct arguments.

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

- Doclet

```java
public Doclet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

============ METHOD DETAIL ==========

- Method Detail

- start

```java
public static boolean start​(
RootDoc
root)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Generate documentation here.
This method is required for all doclets.

**Parameters:** root

- Supply the RootDoc to the method.
**Returns:** true on success.

- optionLength

```java
public static int optionLength​(
String
option)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check for doclet-added options. Returns the number of
arguments you must specify on the command line for the
given option. For example, "-d docs" would return 2.

This method is required if the doclet contains any options.
If this method is missing, Javadoc will print an invalid flag
error for every option.

**Parameters:** option

- the option for which the number of arguements is returned.
**Returns:** number of arguments on the command line for an option
including the option name itself. Zero return means
option not known. Negative value means error occurred.

- validOptions

```java
public static boolean validOptions​(
String
[][] options,

DocErrorReporter
reporter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check that options have the correct arguments.

This method is not required, but is recommended,
as every option will be considered valid if this method
is not present. It will default gracefully (to true)
if absent.

Printing option related error messages (using the provided
DocErrorReporter) is the responsibility of this method.

**Parameters:** options

- Supply valid options as an array of Strings.
**Parameters:** reporter

- The DocErrorReporter responsible for these options.
**Returns:** true if the options are valid.

- languageVersion

```java
public static
LanguageVersion
languageVersion()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the version of the Java Programming Language supported
by this doclet.

This method is required by any doclet supporting a language version
newer than 1.1.

**Returns:** the language version supported by this doclet.
**Since:** 1.5

Constructor Detail

- Doclet

```java
public Doclet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### Constructor Detail

Doclet

```java
public Doclet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

---

#### Doclet

public Doclet()

Method Detail

- start

```java
public static boolean start​(
RootDoc
root)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Generate documentation here.
This method is required for all doclets.

**Parameters:** root

- Supply the RootDoc to the method.
**Returns:** true on success.

- optionLength

```java
public static int optionLength​(
String
option)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check for doclet-added options. Returns the number of
arguments you must specify on the command line for the
given option. For example, "-d docs" would return 2.

This method is required if the doclet contains any options.
If this method is missing, Javadoc will print an invalid flag
error for every option.

**Parameters:** option

- the option for which the number of arguements is returned.
**Returns:** number of arguments on the command line for an option
including the option name itself. Zero return means
option not known. Negative value means error occurred.

- validOptions

```java
public static boolean validOptions​(
String
[][] options,

DocErrorReporter
reporter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check that options have the correct arguments.

This method is not required, but is recommended,
as every option will be considered valid if this method
is not present. It will default gracefully (to true)
if absent.

Printing option related error messages (using the provided
DocErrorReporter) is the responsibility of this method.

**Parameters:** options

- Supply valid options as an array of Strings.
**Parameters:** reporter

- The DocErrorReporter responsible for these options.
**Returns:** true if the options are valid.

- languageVersion

```java
public static
LanguageVersion
languageVersion()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the version of the Java Programming Language supported
by this doclet.

This method is required by any doclet supporting a language version
newer than 1.1.

**Returns:** the language version supported by this doclet.
**Since:** 1.5

---

#### Method Detail

start

```java
public static boolean start​(
RootDoc
root)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Generate documentation here.
This method is required for all doclets.

**Parameters:** root

- Supply the RootDoc to the method.
**Returns:** true on success.

---

#### start

public static boolean start​(

RootDoc

root)

Generate documentation here.
This method is required for all doclets.

optionLength

```java
public static int optionLength​(
String
option)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check for doclet-added options. Returns the number of
arguments you must specify on the command line for the
given option. For example, "-d docs" would return 2.

This method is required if the doclet contains any options.
If this method is missing, Javadoc will print an invalid flag
error for every option.

**Parameters:** option

- the option for which the number of arguements is returned.
**Returns:** number of arguments on the command line for an option
including the option name itself. Zero return means
option not known. Negative value means error occurred.

---

#### optionLength

public static int optionLength​(

String

option)

Check for doclet-added options. Returns the number of
arguments you must specify on the command line for the
given option. For example, "-d docs" would return 2.

This method is required if the doclet contains any options.
If this method is missing, Javadoc will print an invalid flag
error for every option.

This method is required if the doclet contains any options.
If this method is missing, Javadoc will print an invalid flag
error for every option.

validOptions

```java
public static boolean validOptions​(
String
[][] options,

DocErrorReporter
reporter)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Check that options have the correct arguments.

This method is not required, but is recommended,
as every option will be considered valid if this method
is not present. It will default gracefully (to true)
if absent.

Printing option related error messages (using the provided
DocErrorReporter) is the responsibility of this method.

**Parameters:** options

- Supply valid options as an array of Strings.
**Parameters:** reporter

- The DocErrorReporter responsible for these options.
**Returns:** true if the options are valid.

---

#### validOptions

public static boolean validOptions​(

String

[][] options,

DocErrorReporter

reporter)

Check that options have the correct arguments.

This method is not required, but is recommended,
as every option will be considered valid if this method
is not present. It will default gracefully (to true)
if absent.

Printing option related error messages (using the provided
DocErrorReporter) is the responsibility of this method.

This method is not required, but is recommended,
as every option will be considered valid if this method
is not present. It will default gracefully (to true)
if absent.

Printing option related error messages (using the provided
DocErrorReporter) is the responsibility of this method.

Printing option related error messages (using the provided
DocErrorReporter) is the responsibility of this method.

languageVersion

```java
public static
LanguageVersion
languageVersion()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the version of the Java Programming Language supported
by this doclet.

This method is required by any doclet supporting a language version
newer than 1.1.

**Returns:** the language version supported by this doclet.
**Since:** 1.5

---

#### languageVersion

public static

LanguageVersion

languageVersion()

Return the version of the Java Programming Language supported
by this doclet.

This method is required by any doclet supporting a language version
newer than 1.1.

This method is required by any doclet supporting a language version
newer than 1.1.

---


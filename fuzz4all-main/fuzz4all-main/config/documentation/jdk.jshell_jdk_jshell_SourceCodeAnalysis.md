# Class SourceCodeAnalysis

**Source:** `jdk.jshell\jdk\jshell\SourceCodeAnalysis.html`

### Class Description

```java
public abstract class
SourceCodeAnalysis

extends
Object
```

Provides analysis utilities for source code input.
Optional functionality that provides for a richer interactive experience.
Includes completion analysis:
Is the input a complete snippet of code?
Do I need to prompt for more input?
Would adding a semicolon make it complete?
Is there more than one snippet?
etc.
Also includes completion suggestions, as might be used in tab-completion.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public abstract
SourceCodeAnalysis.CompletionInfo
analyzeCompletion​(
String
input)

Given an input string, find the first snippet of code (one statement,
definition, import, or expression) and evaluate if it is complete.

**Parameters:**
- input

- the input source string

**Returns:**
- a CompletionInfo instance with location and completeness info

---

#### public abstract
List
<
SourceCodeAnalysis.Suggestion
> completionSuggestions​(
String
input,
int cursor,
int[] anchor)

Compute possible follow-ups for the given input.
Uses information from the current

JShell

state, including
type information, to filter the suggestions.

**Parameters:**
- input

- the user input, so far
- cursor

- the current position of the cursors in the given

input

text
- anchor

- outgoing parameter - when an option will be completed, the text between
the anchor and cursor will be deleted and replaced with the given option

**Returns:**
- list of candidate continuations of the given input.

---

#### public abstract
List
<
SourceCodeAnalysis.Documentation
> documentation​(
String
input,
int cursor,
boolean computeJavadoc)

Compute documentation for the given user's input. Multiple

Documentation

objects may
be returned when multiple elements match the user's input (like for overloaded methods).

**Parameters:**
- input

- the snippet the user wrote so far
- cursor

- the current position of the cursors in the given

input

text
- computeJavadoc

- true if the javadoc for the given input should be computed in
addition to the signature

**Returns:**
- the documentations for the given user's input, if multiple elements match the input,
multiple

Documentation

objects are returned.

---

#### public abstract
String
analyzeType​(
String
code,
int cursor)

Infer the type of the given expression. The expression spans from the beginning of

code

to the given

cursor

position. Returns null if the type of the expression cannot
be inferred.

**Parameters:**
- code

- the expression for which the type should be inferred
- cursor

- current cursor position in the given code

**Returns:**
- the inferred type, or null if it cannot be inferred

---

#### public abstract
SourceCodeAnalysis.QualifiedNames
listQualifiedNames​(
String
code,
int cursor)

List qualified names known for the simple name in the given code immediately
to the left of the given cursor position. The qualified names are gathered by inspecting the
classpath used by eval (see

JShell.addToClasspath(java.lang.String)

).

**Parameters:**
- code

- the expression for which the candidate qualified names should be computed
- cursor

- current cursor position in the given code

**Returns:**
- the known qualified names

---

#### public abstract
SourceCodeAnalysis.SnippetWrapper
wrapper​(
Snippet
snippet)

Returns the wrapper information for the

Snippet

. The wrapper changes as
the environment changes, so calls to this method at different times may
yield different results.

**Parameters:**
- snippet

- the

Snippet

from which to retrieve the wrapper

**Returns:**
- information on the wrapper

---

#### public abstract
List
<
SourceCodeAnalysis.SnippetWrapper
> wrappers​(
String
input)

Returns the wrapper information for the snippet within the
input source string.

Wrapper information for malformed and incomplete
snippets also generate wrappers. The list is in snippet encounter
order. The wrapper changes as the environment changes, so calls to this
method at different times may yield different results.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

analyzeCompletion(String)

.

The wrapper may not match that returned by

wrapper(Snippet)

,
were the source converted to a

Snippet

.

**Parameters:**
- input

- the source input from which to generate wrappers

**Returns:**
- a list of wrapper information

---

#### public abstract
List
<
Snippet
> sourceToSnippets​(
String
input)

Converts the source code of a snippet into a

Snippet

object (or
list of

Snippet

objects in the case of some var declarations,
e.g.: int x, y, z;).
Does not install the snippets: declarations are not
accessible by other snippets; imports are not added.
Does not execute the snippets.

Queries may be done on the

Snippet

object. The

Snippet.id()

will be

"*UNASSOCIATED*"

.
The returned snippets are not associated with the

JShell

instance, so attempts to pass them to

JShell

methods will throw an

IllegalArgumentException

.
They will not appear in queries for snippets --
for example,

JShell.snippets()

.

Restrictions on the input are as in

JShell.eval

.

Only preliminary compilation is performed, sufficient to build the

Snippet

. Snippets known to be erroneous, are returned as

ErroneousSnippet

, other snippets may or may not be in error.

**Parameters:**
- input

- The input String to convert

**Returns:**
- usually a singleton list of Snippet, but may be empty or multiple

**Throws:**
- IllegalStateException

- if the

JShell

instance is closed.

---

#### public abstract
Collection
<
Snippet
> dependents​(
Snippet
snippet)

Returns a collection of

Snippet

s which might need updating if the
given

Snippet

is updated. The returned collection is designed to
be inclusive and may include many false positives.

**Parameters:**
- snippet

- the

Snippet

whose dependents are requested

**Returns:**
- the collection of dependents

---

### Additional Sections

#### Class SourceCodeAnalysis

java.lang.Object

- jdk.jshell.SourceCodeAnalysis

jdk.jshell.SourceCodeAnalysis

```java
public abstract class
SourceCodeAnalysis

extends
Object
```

Provides analysis utilities for source code input.
Optional functionality that provides for a richer interactive experience.
Includes completion analysis:
Is the input a complete snippet of code?
Do I need to prompt for more input?
Would adding a semicolon make it complete?
Is there more than one snippet?
etc.
Also includes completion suggestions, as might be used in tab-completion.

**Since:** 9

public abstract class

SourceCodeAnalysis

extends

Object

Provides analysis utilities for source code input.
Optional functionality that provides for a richer interactive experience.
Includes completion analysis:
Is the input a complete snippet of code?
Do I need to prompt for more input?
Would adding a semicolon make it complete?
Is there more than one snippet?
etc.
Also includes completion suggestions, as might be used in tab-completion.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SourceCodeAnalysis.Completeness

Describes the completeness of the given input.

static interface

SourceCodeAnalysis.CompletionInfo

The result of

analyzeCompletion(String input)

.

static interface

SourceCodeAnalysis.Documentation

A documentation for a candidate for continuation of the given user's input.

static class

SourceCodeAnalysis.QualifiedNames

List of possible qualified names.

static interface

SourceCodeAnalysis.SnippetWrapper

The wrapping of a snippet of Java source into valid top-level Java
source.

static interface

SourceCodeAnalysis.Suggestion

A candidate for continuation of the given user's input.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

SourceCodeAnalysis.CompletionInfo

analyzeCompletion

​(

String

input)

Given an input string, find the first snippet of code (one statement,
definition, import, or expression) and evaluate if it is complete.

abstract

String

analyzeType

​(

String

code,
int cursor)

Infer the type of the given expression.

abstract

List

<

SourceCodeAnalysis.Suggestion

>

completionSuggestions

​(

String

input,
int cursor,
int[] anchor)

Compute possible follow-ups for the given input.

abstract

Collection

<

Snippet

>

dependents

​(

Snippet

snippet)

Returns a collection of

Snippet

s which might need updating if the
given

Snippet

is updated.

abstract

List

<

SourceCodeAnalysis.Documentation

>

documentation

​(

String

input,
int cursor,
boolean computeJavadoc)

Compute documentation for the given user's input.

abstract

SourceCodeAnalysis.QualifiedNames

listQualifiedNames

​(

String

code,
int cursor)

List qualified names known for the simple name in the given code immediately
to the left of the given cursor position.

abstract

List

<

Snippet

>

sourceToSnippets

​(

String

input)

Converts the source code of a snippet into a

Snippet

object (or
list of

Snippet

objects in the case of some var declarations,
e.g.: int x, y, z;).

abstract

SourceCodeAnalysis.SnippetWrapper

wrapper

​(

Snippet

snippet)

Returns the wrapper information for the

Snippet

.

abstract

List

<

SourceCodeAnalysis.SnippetWrapper

>

wrappers

​(

String

input)

Returns the wrapper information for the snippet within the
input source string.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SourceCodeAnalysis.Completeness

Describes the completeness of the given input.

static interface

SourceCodeAnalysis.CompletionInfo

The result of

analyzeCompletion(String input)

.

static interface

SourceCodeAnalysis.Documentation

A documentation for a candidate for continuation of the given user's input.

static class

SourceCodeAnalysis.QualifiedNames

List of possible qualified names.

static interface

SourceCodeAnalysis.SnippetWrapper

The wrapping of a snippet of Java source into valid top-level Java
source.

static interface

SourceCodeAnalysis.Suggestion

A candidate for continuation of the given user's input.

---

#### Nested Class Summary

Describes the completeness of the given input.

The result of

analyzeCompletion(String input)

.

A documentation for a candidate for continuation of the given user's input.

List of possible qualified names.

The wrapping of a snippet of Java source into valid top-level Java
source.

A candidate for continuation of the given user's input.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

SourceCodeAnalysis.CompletionInfo

analyzeCompletion

​(

String

input)

Given an input string, find the first snippet of code (one statement,
definition, import, or expression) and evaluate if it is complete.

abstract

String

analyzeType

​(

String

code,
int cursor)

Infer the type of the given expression.

abstract

List

<

SourceCodeAnalysis.Suggestion

>

completionSuggestions

​(

String

input,
int cursor,
int[] anchor)

Compute possible follow-ups for the given input.

abstract

Collection

<

Snippet

>

dependents

​(

Snippet

snippet)

Returns a collection of

Snippet

s which might need updating if the
given

Snippet

is updated.

abstract

List

<

SourceCodeAnalysis.Documentation

>

documentation

​(

String

input,
int cursor,
boolean computeJavadoc)

Compute documentation for the given user's input.

abstract

SourceCodeAnalysis.QualifiedNames

listQualifiedNames

​(

String

code,
int cursor)

List qualified names known for the simple name in the given code immediately
to the left of the given cursor position.

abstract

List

<

Snippet

>

sourceToSnippets

​(

String

input)

Converts the source code of a snippet into a

Snippet

object (or
list of

Snippet

objects in the case of some var declarations,
e.g.: int x, y, z;).

abstract

SourceCodeAnalysis.SnippetWrapper

wrapper

​(

Snippet

snippet)

Returns the wrapper information for the

Snippet

.

abstract

List

<

SourceCodeAnalysis.SnippetWrapper

>

wrappers

​(

String

input)

Returns the wrapper information for the snippet within the
input source string.

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

Given an input string, find the first snippet of code (one statement,
definition, import, or expression) and evaluate if it is complete.

Infer the type of the given expression.

Compute possible follow-ups for the given input.

Returns a collection of

Snippet

s which might need updating if the
given

Snippet

is updated.

Compute documentation for the given user's input.

List qualified names known for the simple name in the given code immediately
to the left of the given cursor position.

Converts the source code of a snippet into a

Snippet

object (or
list of

Snippet

objects in the case of some var declarations,
e.g.: int x, y, z;).

Returns the wrapper information for the

Snippet

.

Returns the wrapper information for the snippet within the
input source string.

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

============ METHOD DETAIL ==========

- Method Detail

- analyzeCompletion

```java
public abstract
SourceCodeAnalysis.CompletionInfo
analyzeCompletion​(
String
input)
```

Given an input string, find the first snippet of code (one statement,
definition, import, or expression) and evaluate if it is complete.

**Parameters:** input

- the input source string
**Returns:** a CompletionInfo instance with location and completeness info

- completionSuggestions

```java
public abstract
List
<
SourceCodeAnalysis.Suggestion
> completionSuggestions​(
String
input,
int cursor,
int[] anchor)
```

Compute possible follow-ups for the given input.
Uses information from the current

JShell

state, including
type information, to filter the suggestions.

**Parameters:** input

- the user input, so far
**Parameters:** cursor

- the current position of the cursors in the given

input

text
**Parameters:** anchor

- outgoing parameter - when an option will be completed, the text between
the anchor and cursor will be deleted and replaced with the given option
**Returns:** list of candidate continuations of the given input.

- documentation

```java
public abstract
List
<
SourceCodeAnalysis.Documentation
> documentation​(
String
input,
int cursor,
boolean computeJavadoc)
```

Compute documentation for the given user's input. Multiple

Documentation

objects may
be returned when multiple elements match the user's input (like for overloaded methods).

**Parameters:** input

- the snippet the user wrote so far
**Parameters:** cursor

- the current position of the cursors in the given

input

text
**Parameters:** computeJavadoc

- true if the javadoc for the given input should be computed in
addition to the signature
**Returns:** the documentations for the given user's input, if multiple elements match the input,
multiple

Documentation

objects are returned.

- analyzeType

```java
public abstract
String
analyzeType​(
String
code,
int cursor)
```

Infer the type of the given expression. The expression spans from the beginning of

code

to the given

cursor

position. Returns null if the type of the expression cannot
be inferred.

**Parameters:** code

- the expression for which the type should be inferred
**Parameters:** cursor

- current cursor position in the given code
**Returns:** the inferred type, or null if it cannot be inferred

- listQualifiedNames

```java
public abstract
SourceCodeAnalysis.QualifiedNames
listQualifiedNames​(
String
code,
int cursor)
```

List qualified names known for the simple name in the given code immediately
to the left of the given cursor position. The qualified names are gathered by inspecting the
classpath used by eval (see

JShell.addToClasspath(java.lang.String)

).

**Parameters:** code

- the expression for which the candidate qualified names should be computed
**Parameters:** cursor

- current cursor position in the given code
**Returns:** the known qualified names

- wrapper

```java
public abstract
SourceCodeAnalysis.SnippetWrapper
wrapper​(
Snippet
snippet)
```

Returns the wrapper information for the

Snippet

. The wrapper changes as
the environment changes, so calls to this method at different times may
yield different results.

**Parameters:** snippet

- the

Snippet

from which to retrieve the wrapper
**Returns:** information on the wrapper

- wrappers

```java
public abstract
List
<
SourceCodeAnalysis.SnippetWrapper
> wrappers​(
String
input)
```

Returns the wrapper information for the snippet within the
input source string.

Wrapper information for malformed and incomplete
snippets also generate wrappers. The list is in snippet encounter
order. The wrapper changes as the environment changes, so calls to this
method at different times may yield different results.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

analyzeCompletion(String)

.

The wrapper may not match that returned by

wrapper(Snippet)

,
were the source converted to a

Snippet

.

**Parameters:** input

- the source input from which to generate wrappers
**Returns:** a list of wrapper information

- sourceToSnippets

```java
public abstract
List
<
Snippet
> sourceToSnippets​(
String
input)
```

Converts the source code of a snippet into a

Snippet

object (or
list of

Snippet

objects in the case of some var declarations,
e.g.: int x, y, z;).
Does not install the snippets: declarations are not
accessible by other snippets; imports are not added.
Does not execute the snippets.

Queries may be done on the

Snippet

object. The

Snippet.id()

will be

"*UNASSOCIATED*"

.
The returned snippets are not associated with the

JShell

instance, so attempts to pass them to

JShell

methods will throw an

IllegalArgumentException

.
They will not appear in queries for snippets --
for example,

JShell.snippets()

.

Restrictions on the input are as in

JShell.eval

.

Only preliminary compilation is performed, sufficient to build the

Snippet

. Snippets known to be erroneous, are returned as

ErroneousSnippet

, other snippets may or may not be in error.

**Parameters:** input

- The input String to convert
**Returns:** usually a singleton list of Snippet, but may be empty or multiple
**Throws:** IllegalStateException

- if the

JShell

instance is closed.

- dependents

```java
public abstract
Collection
<
Snippet
> dependents​(
Snippet
snippet)
```

Returns a collection of

Snippet

s which might need updating if the
given

Snippet

is updated. The returned collection is designed to
be inclusive and may include many false positives.

**Parameters:** snippet

- the

Snippet

whose dependents are requested
**Returns:** the collection of dependents

Method Detail

- analyzeCompletion

```java
public abstract
SourceCodeAnalysis.CompletionInfo
analyzeCompletion​(
String
input)
```

Given an input string, find the first snippet of code (one statement,
definition, import, or expression) and evaluate if it is complete.

**Parameters:** input

- the input source string
**Returns:** a CompletionInfo instance with location and completeness info

- completionSuggestions

```java
public abstract
List
<
SourceCodeAnalysis.Suggestion
> completionSuggestions​(
String
input,
int cursor,
int[] anchor)
```

Compute possible follow-ups for the given input.
Uses information from the current

JShell

state, including
type information, to filter the suggestions.

**Parameters:** input

- the user input, so far
**Parameters:** cursor

- the current position of the cursors in the given

input

text
**Parameters:** anchor

- outgoing parameter - when an option will be completed, the text between
the anchor and cursor will be deleted and replaced with the given option
**Returns:** list of candidate continuations of the given input.

- documentation

```java
public abstract
List
<
SourceCodeAnalysis.Documentation
> documentation​(
String
input,
int cursor,
boolean computeJavadoc)
```

Compute documentation for the given user's input. Multiple

Documentation

objects may
be returned when multiple elements match the user's input (like for overloaded methods).

**Parameters:** input

- the snippet the user wrote so far
**Parameters:** cursor

- the current position of the cursors in the given

input

text
**Parameters:** computeJavadoc

- true if the javadoc for the given input should be computed in
addition to the signature
**Returns:** the documentations for the given user's input, if multiple elements match the input,
multiple

Documentation

objects are returned.

- analyzeType

```java
public abstract
String
analyzeType​(
String
code,
int cursor)
```

Infer the type of the given expression. The expression spans from the beginning of

code

to the given

cursor

position. Returns null if the type of the expression cannot
be inferred.

**Parameters:** code

- the expression for which the type should be inferred
**Parameters:** cursor

- current cursor position in the given code
**Returns:** the inferred type, or null if it cannot be inferred

- listQualifiedNames

```java
public abstract
SourceCodeAnalysis.QualifiedNames
listQualifiedNames​(
String
code,
int cursor)
```

List qualified names known for the simple name in the given code immediately
to the left of the given cursor position. The qualified names are gathered by inspecting the
classpath used by eval (see

JShell.addToClasspath(java.lang.String)

).

**Parameters:** code

- the expression for which the candidate qualified names should be computed
**Parameters:** cursor

- current cursor position in the given code
**Returns:** the known qualified names

- wrapper

```java
public abstract
SourceCodeAnalysis.SnippetWrapper
wrapper​(
Snippet
snippet)
```

Returns the wrapper information for the

Snippet

. The wrapper changes as
the environment changes, so calls to this method at different times may
yield different results.

**Parameters:** snippet

- the

Snippet

from which to retrieve the wrapper
**Returns:** information on the wrapper

- wrappers

```java
public abstract
List
<
SourceCodeAnalysis.SnippetWrapper
> wrappers​(
String
input)
```

Returns the wrapper information for the snippet within the
input source string.

Wrapper information for malformed and incomplete
snippets also generate wrappers. The list is in snippet encounter
order. The wrapper changes as the environment changes, so calls to this
method at different times may yield different results.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

analyzeCompletion(String)

.

The wrapper may not match that returned by

wrapper(Snippet)

,
were the source converted to a

Snippet

.

**Parameters:** input

- the source input from which to generate wrappers
**Returns:** a list of wrapper information

- sourceToSnippets

```java
public abstract
List
<
Snippet
> sourceToSnippets​(
String
input)
```

Converts the source code of a snippet into a

Snippet

object (or
list of

Snippet

objects in the case of some var declarations,
e.g.: int x, y, z;).
Does not install the snippets: declarations are not
accessible by other snippets; imports are not added.
Does not execute the snippets.

Queries may be done on the

Snippet

object. The

Snippet.id()

will be

"*UNASSOCIATED*"

.
The returned snippets are not associated with the

JShell

instance, so attempts to pass them to

JShell

methods will throw an

IllegalArgumentException

.
They will not appear in queries for snippets --
for example,

JShell.snippets()

.

Restrictions on the input are as in

JShell.eval

.

Only preliminary compilation is performed, sufficient to build the

Snippet

. Snippets known to be erroneous, are returned as

ErroneousSnippet

, other snippets may or may not be in error.

**Parameters:** input

- The input String to convert
**Returns:** usually a singleton list of Snippet, but may be empty or multiple
**Throws:** IllegalStateException

- if the

JShell

instance is closed.

- dependents

```java
public abstract
Collection
<
Snippet
> dependents​(
Snippet
snippet)
```

Returns a collection of

Snippet

s which might need updating if the
given

Snippet

is updated. The returned collection is designed to
be inclusive and may include many false positives.

**Parameters:** snippet

- the

Snippet

whose dependents are requested
**Returns:** the collection of dependents

---

#### Method Detail

analyzeCompletion

```java
public abstract
SourceCodeAnalysis.CompletionInfo
analyzeCompletion​(
String
input)
```

Given an input string, find the first snippet of code (one statement,
definition, import, or expression) and evaluate if it is complete.

**Parameters:** input

- the input source string
**Returns:** a CompletionInfo instance with location and completeness info

---

#### analyzeCompletion

public abstract

SourceCodeAnalysis.CompletionInfo

analyzeCompletion​(

String

input)

Given an input string, find the first snippet of code (one statement,
definition, import, or expression) and evaluate if it is complete.

completionSuggestions

```java
public abstract
List
<
SourceCodeAnalysis.Suggestion
> completionSuggestions​(
String
input,
int cursor,
int[] anchor)
```

Compute possible follow-ups for the given input.
Uses information from the current

JShell

state, including
type information, to filter the suggestions.

**Parameters:** input

- the user input, so far
**Parameters:** cursor

- the current position of the cursors in the given

input

text
**Parameters:** anchor

- outgoing parameter - when an option will be completed, the text between
the anchor and cursor will be deleted and replaced with the given option
**Returns:** list of candidate continuations of the given input.

---

#### completionSuggestions

public abstract

List

<

SourceCodeAnalysis.Suggestion

> completionSuggestions​(

String

input,
int cursor,
int[] anchor)

Compute possible follow-ups for the given input.
Uses information from the current

JShell

state, including
type information, to filter the suggestions.

documentation

```java
public abstract
List
<
SourceCodeAnalysis.Documentation
> documentation​(
String
input,
int cursor,
boolean computeJavadoc)
```

Compute documentation for the given user's input. Multiple

Documentation

objects may
be returned when multiple elements match the user's input (like for overloaded methods).

**Parameters:** input

- the snippet the user wrote so far
**Parameters:** cursor

- the current position of the cursors in the given

input

text
**Parameters:** computeJavadoc

- true if the javadoc for the given input should be computed in
addition to the signature
**Returns:** the documentations for the given user's input, if multiple elements match the input,
multiple

Documentation

objects are returned.

---

#### documentation

public abstract

List

<

SourceCodeAnalysis.Documentation

> documentation​(

String

input,
int cursor,
boolean computeJavadoc)

Compute documentation for the given user's input. Multiple

Documentation

objects may
be returned when multiple elements match the user's input (like for overloaded methods).

analyzeType

```java
public abstract
String
analyzeType​(
String
code,
int cursor)
```

Infer the type of the given expression. The expression spans from the beginning of

code

to the given

cursor

position. Returns null if the type of the expression cannot
be inferred.

**Parameters:** code

- the expression for which the type should be inferred
**Parameters:** cursor

- current cursor position in the given code
**Returns:** the inferred type, or null if it cannot be inferred

---

#### analyzeType

public abstract

String

analyzeType​(

String

code,
int cursor)

Infer the type of the given expression. The expression spans from the beginning of

code

to the given

cursor

position. Returns null if the type of the expression cannot
be inferred.

listQualifiedNames

```java
public abstract
SourceCodeAnalysis.QualifiedNames
listQualifiedNames​(
String
code,
int cursor)
```

List qualified names known for the simple name in the given code immediately
to the left of the given cursor position. The qualified names are gathered by inspecting the
classpath used by eval (see

JShell.addToClasspath(java.lang.String)

).

**Parameters:** code

- the expression for which the candidate qualified names should be computed
**Parameters:** cursor

- current cursor position in the given code
**Returns:** the known qualified names

---

#### listQualifiedNames

public abstract

SourceCodeAnalysis.QualifiedNames

listQualifiedNames​(

String

code,
int cursor)

List qualified names known for the simple name in the given code immediately
to the left of the given cursor position. The qualified names are gathered by inspecting the
classpath used by eval (see

JShell.addToClasspath(java.lang.String)

).

wrapper

```java
public abstract
SourceCodeAnalysis.SnippetWrapper
wrapper​(
Snippet
snippet)
```

Returns the wrapper information for the

Snippet

. The wrapper changes as
the environment changes, so calls to this method at different times may
yield different results.

**Parameters:** snippet

- the

Snippet

from which to retrieve the wrapper
**Returns:** information on the wrapper

---

#### wrapper

public abstract

SourceCodeAnalysis.SnippetWrapper

wrapper​(

Snippet

snippet)

Returns the wrapper information for the

Snippet

. The wrapper changes as
the environment changes, so calls to this method at different times may
yield different results.

wrappers

```java
public abstract
List
<
SourceCodeAnalysis.SnippetWrapper
> wrappers​(
String
input)
```

Returns the wrapper information for the snippet within the
input source string.

Wrapper information for malformed and incomplete
snippets also generate wrappers. The list is in snippet encounter
order. The wrapper changes as the environment changes, so calls to this
method at different times may yield different results.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

analyzeCompletion(String)

.

The wrapper may not match that returned by

wrapper(Snippet)

,
were the source converted to a

Snippet

.

**Parameters:** input

- the source input from which to generate wrappers
**Returns:** a list of wrapper information

---

#### wrappers

public abstract

List

<

SourceCodeAnalysis.SnippetWrapper

> wrappers​(

String

input)

Returns the wrapper information for the snippet within the
input source string.

Wrapper information for malformed and incomplete
snippets also generate wrappers. The list is in snippet encounter
order. The wrapper changes as the environment changes, so calls to this
method at different times may yield different results.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

analyzeCompletion(String)

.

The wrapper may not match that returned by

wrapper(Snippet)

,
were the source converted to a

Snippet

.

Wrapper information for malformed and incomplete
snippets also generate wrappers. The list is in snippet encounter
order. The wrapper changes as the environment changes, so calls to this
method at different times may yield different results.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

analyzeCompletion(String)

.

The wrapper may not match that returned by

wrapper(Snippet)

,
were the source converted to a

Snippet

.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

analyzeCompletion(String)

.

The wrapper may not match that returned by

wrapper(Snippet)

,
were the source converted to a

Snippet

.

The wrapper may not match that returned by

wrapper(Snippet)

,
were the source converted to a

Snippet

.

sourceToSnippets

```java
public abstract
List
<
Snippet
> sourceToSnippets​(
String
input)
```

Converts the source code of a snippet into a

Snippet

object (or
list of

Snippet

objects in the case of some var declarations,
e.g.: int x, y, z;).
Does not install the snippets: declarations are not
accessible by other snippets; imports are not added.
Does not execute the snippets.

Queries may be done on the

Snippet

object. The

Snippet.id()

will be

"*UNASSOCIATED*"

.
The returned snippets are not associated with the

JShell

instance, so attempts to pass them to

JShell

methods will throw an

IllegalArgumentException

.
They will not appear in queries for snippets --
for example,

JShell.snippets()

.

Restrictions on the input are as in

JShell.eval

.

Only preliminary compilation is performed, sufficient to build the

Snippet

. Snippets known to be erroneous, are returned as

ErroneousSnippet

, other snippets may or may not be in error.

**Parameters:** input

- The input String to convert
**Returns:** usually a singleton list of Snippet, but may be empty or multiple
**Throws:** IllegalStateException

- if the

JShell

instance is closed.

---

#### sourceToSnippets

public abstract

List

<

Snippet

> sourceToSnippets​(

String

input)

Converts the source code of a snippet into a

Snippet

object (or
list of

Snippet

objects in the case of some var declarations,
e.g.: int x, y, z;).
Does not install the snippets: declarations are not
accessible by other snippets; imports are not added.
Does not execute the snippets.

Queries may be done on the

Snippet

object. The

Snippet.id()

will be

"*UNASSOCIATED*"

.
The returned snippets are not associated with the

JShell

instance, so attempts to pass them to

JShell

methods will throw an

IllegalArgumentException

.
They will not appear in queries for snippets --
for example,

JShell.snippets()

.

Restrictions on the input are as in

JShell.eval

.

Only preliminary compilation is performed, sufficient to build the

Snippet

. Snippets known to be erroneous, are returned as

ErroneousSnippet

, other snippets may or may not be in error.

Queries may be done on the

Snippet

object. The

Snippet.id()

will be

"*UNASSOCIATED*"

.
The returned snippets are not associated with the

JShell

instance, so attempts to pass them to

JShell

methods will throw an

IllegalArgumentException

.
They will not appear in queries for snippets --
for example,

JShell.snippets()

.

Restrictions on the input are as in

JShell.eval

.

Only preliminary compilation is performed, sufficient to build the

Snippet

. Snippets known to be erroneous, are returned as

ErroneousSnippet

, other snippets may or may not be in error.

Restrictions on the input are as in

JShell.eval

.

Only preliminary compilation is performed, sufficient to build the

Snippet

. Snippets known to be erroneous, are returned as

ErroneousSnippet

, other snippets may or may not be in error.

Only preliminary compilation is performed, sufficient to build the

Snippet

. Snippets known to be erroneous, are returned as

ErroneousSnippet

, other snippets may or may not be in error.

dependents

```java
public abstract
Collection
<
Snippet
> dependents​(
Snippet
snippet)
```

Returns a collection of

Snippet

s which might need updating if the
given

Snippet

is updated. The returned collection is designed to
be inclusive and may include many false positives.

**Parameters:** snippet

- the

Snippet

whose dependents are requested
**Returns:** the collection of dependents

---

#### dependents

public abstract

Collection

<

Snippet

> dependents​(

Snippet

snippet)

Returns a collection of

Snippet

s which might need updating if the
given

Snippet

is updated. The returned collection is designed to
be inclusive and may include many false positives.

---


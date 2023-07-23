/*
 *  This function below was extracted from the OpenBSD source project,
 *  specifically the `cat.c` file in the `bin/cat` directory. It was
 *  retrieved from https://github.com/openbsd/src/blob/0b6813b0c5547848ad4bfd1021622647a4059935/bin/cat/cat.c#L111-L143
 *  on July 23, 2023.
 *
 *  The comment header for that file has been moved to below the `cat_file`
 *  function. It includes the license that this code is governed by.
 */

void
cat_file(const char *path)
{
	FILE *fp;
	int fd;

	if (bflag || eflag || nflag || sflag || tflag || vflag) {
		if (path == NULL || strcmp(path, "-") == 0) {
			cook_buf(stdin, "stdin");
			clearerr(stdin);
		} else {
			if ((fp = fopen(path, "r")) == NULL) {
				warn("%s", path);
				rval = 1;
				return;
			}
			cook_buf(fp, path);
			fclose(fp);
		}
	} else {
		if (path == NULL || strcmp(path, "-") == 0) {
			raw_cat(STDIN_FILENO, "stdin");
		} else {
			if ((fd = open(path, O_RDONLY)) == -1) {
				warn("%s", path);
				rval = 1;
				return;
			}
			raw_cat(fd, path);
			close(fd);
		}
	}
}

/*
 * Copyright (c) 1989, 1993
 *	The Regents of the University of California.  All rights reserved.
 *
 * This code is derived from software contributed to Berkeley by
 * Kevin Fall.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

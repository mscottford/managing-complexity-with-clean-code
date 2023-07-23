// The `sortBranches` function below is from the `vscode-gitlens` project. 
// It was copied from https://github.com/gitkraken/vscode-gitlens/blob/60b4983dad5358c3e254c49a1555c22eb85b1d5d/src/git/models/branch.ts#L256-L304
// on July 23, 2023. 
//
// The license that the code was published under has been
// included at the bottom of this file.

export function sortBranches(branches: GitBranch[], options?: BranchSortOptions) {
    options = { current: true, orderBy: configuration.get('sortBranchesBy'), ...options };

    switch (options.orderBy) {
        case BranchSorting.DateAsc:
            return branches.sort(
                (a, b) =>
                    (options!.missingUpstream ? (a.upstream?.missing ? -1 : 1) - (b.upstream?.missing ? -1 : 1) : 0) ||
                    (options!.current ? (a.current ? -1 : 1) - (b.current ? -1 : 1) : 0) ||
                    (a.starred ? -1 : 1) - (b.starred ? -1 : 1) ||
                    (b.remote ? -1 : 1) - (a.remote ? -1 : 1) ||
                    (a.date == null ? -1 : a.date.getTime()) - (b.date == null ? -1 : b.date.getTime()),
            );
        case BranchSorting.NameAsc:
            return branches.sort(
                (a, b) =>
                    (options!.missingUpstream ? (a.upstream?.missing ? -1 : 1) - (b.upstream?.missing ? -1 : 1) : 0) ||
                    (options!.current ? (a.current ? -1 : 1) - (b.current ? -1 : 1) : 0) ||
                    (a.starred ? -1 : 1) - (b.starred ? -1 : 1) ||
                    (a.name === 'main' ? -1 : 1) - (b.name === 'main' ? -1 : 1) ||
                    (a.name === 'master' ? -1 : 1) - (b.name === 'master' ? -1 : 1) ||
                    (a.name === 'develop' ? -1 : 1) - (b.name === 'develop' ? -1 : 1) ||
                    (b.remote ? -1 : 1) - (a.remote ? -1 : 1) ||
                    sortCompare(a.name, b.name),
            );
        case BranchSorting.NameDesc:
            return branches.sort(
                (a, b) =>
                    (options!.missingUpstream ? (a.upstream?.missing ? -1 : 1) - (b.upstream?.missing ? -1 : 1) : 0) ||
                    (options!.current ? (a.current ? -1 : 1) - (b.current ? -1 : 1) : 0) ||
                    (a.starred ? -1 : 1) - (b.starred ? -1 : 1) ||
                    (a.name === 'main' ? -1 : 1) - (b.name === 'main' ? -1 : 1) ||
                    (a.name === 'master' ? -1 : 1) - (b.name === 'master' ? -1 : 1) ||
                    (a.name === 'develop' ? -1 : 1) - (b.name === 'develop' ? -1 : 1) ||
                    (b.remote ? -1 : 1) - (a.remote ? -1 : 1) ||
                    sortCompare(b.name, a.name),
            );
        case BranchSorting.DateDesc:
        default:
            return branches.sort(
                (a, b) =>
                    (options!.missingUpstream ? (a.upstream?.missing ? -1 : 1) - (b.upstream?.missing ? -1 : 1) : 0) ||
                    (options!.current ? (a.current ? -1 : 1) - (b.current ? -1 : 1) : 0) ||
                    (a.starred ? -1 : 1) - (b.starred ? -1 : 1) ||
                    (b.remote ? -1 : 1) - (a.remote ? -1 : 1) ||
                    (b.date == null ? -1 : b.date.getTime()) - (a.date == null ? -1 : a.date.getTime()),
            );
    }
}

// The license below was copied from https://github.com/gitkraken/vscode-gitlens/blob/60b4983dad5358c3e254c49a1555c22eb85b1d5d/LICENSE
//
// The MIT License (MIT)
//
// Copyright (c) 2021-2023 Axosoft, LLC dba GitKraken ("GitKraken")
// Copyright (c) 2016-2021 Eric Amodio
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

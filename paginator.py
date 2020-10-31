def pagination(filesToDisplay, N=8):        # Postoji problem ako se poveca N na poslednjoj stranici - baca gresku
    currentPage = 1

    if len(filesToDisplay) < N:
        N = len(filesToDisplay)

    pageCount = round(len(filesToDisplay)/N)

    while True:
        print("==================")

        if currentPage == pageCount:
            for i in range((currentPage-1)*N, len(filesToDisplay)):
                print(filesToDisplay[i])
        else:
            for i in range((currentPage-1)*N, currentPage*N):
                print(filesToDisplay[i])

        print("==================")

        pageDisplayString = ""
        if currentPage > 1:
            pageDisplayString += "Prev "


        pageNumStart = 1
        pageNumEnd = pageCount

        if pageCount > 10:
            pageNumEnd = 10

            if currentPage > 6:
                pageNumStart = currentPage - 5
                pageNumEnd = currentPage + 4

                if pageNumEnd > pageCount:
                    pageNumStart = pageNumStart - (pageNumEnd - pageCount)
                    pageNumEnd = pageCount

        for pageNum in range(pageNumStart, pageNumEnd+1):
            if pageNum == currentPage:
                s = "[" + str(pageNum) + "] "
            else:
                s = str(pageNum) + " "
            pageDisplayString += s

        if currentPage != pageCount:
            pageDisplayString += "Next"

        print(pageDisplayString)
        print("==================")
        print("Type 0 to exit")
        option = input("Choose page or type N to change number of entries per page: ")

        if option == "0":
            break

        if option == "N":
            N = -1
            while N < 1 or N > len(filesToDisplay):
                n_input = input("Number of entries per page: ")

                try:
                    N = int(n_input)
                except ValueError:
                    print("Has to be an integer!")
                    continue

            pageCount = round(len(filesToDisplay)/N)
            continue

        if option.lower() == "prev":
            if currentPage > 1:
                currentPage -= 1

            continue

        if option.lower() == "next":
            if currentPage < pageCount:
                currentPage += 1

            continue

        try:
            option = int(option)
        except ValueError:
            print("Incorrect entry!")
            continue

        while option > pageCount or option < 0:
            input_option = input("Page does not exist, type correct entry: ")
            try:
                option = int(input_option)
            except ValueError:
                continue

        currentPage = option